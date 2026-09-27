"""Build/verify the integrated package with a strict manifest; Python stdlib only."""
from pathlib import Path
import argparse
import hashlib
import io
import json
import re
import struct
import zipfile

ROOT = Path(__file__).resolve().parents[1]
PACKAGE = 'ha_ij_direction'
VERSION = 'v0.2.0'
NAME = 'ha_ｉｊ方向頂点移動ツール'
EXPECTED = {'ha_ｉｊ方向移動.vsm', 'ha_ｉｊ方向移動.vss', NAME + '.vst', NAME + '.vss', 'VertexMove.px', 'ha_MeasureDistance.px',
            'ha_PickReferenceAngle.px', 'ha_ij_direction.vwr', 'ha_VSFunctions.vlb',
            'ha_VSFunctions.vwr', 'README.md', 'LICENSE', 'LICENSE-MIT.txt', 'LICENSE-SDK-RUNTIME.md'}


def digest(data):
    return hashlib.sha256(data).hexdigest()


def validate(files):
    assert set(files) == EXPECTED, 'Unexpected/missing files'
    manifest = json.loads((ROOT / 'package-sha256.json').read_text(encoding='utf-8'))
    assert set(manifest) == EXPECTED
    for name, data in files.items():
        assert digest(data) == manifest[name], 'Manifest mismatch: ' + name
        assert not re.search(rb'(?i)(?<![a-z])[a-z]:[\\/]|_VectorScript|VectorworksSDK', data), name
        if name.endswith(('.vss', '.px')):
            source = data.decode('utf-8')
            for inc in re.findall(r'\{\$INCLUDE ([^}]+)\}', source):
                assert inc in files, 'Unresolved INCLUDE: ' + inc
            assert not re.search(r'\{\$\s*DEBUG\s*\}', source, re.I)
    wrapper = files[NAME + '.vst']
    start, size = struct.unpack_from('<II', wrapper, 136)
    assert 144 <= start < start + size <= len(wrapper)
    assert wrapper[start:start+size].decode('utf-8').strip() == '{$INCLUDE ' + NAME + '.vss}'
    menu = files['ha_ｉｊ方向移動.vsm']
    ma, mn = struct.unpack_from('<II', menu, 136)
    assert menu[ma:ma+mn].decode('utf-8').strip() == '{$INCLUDE ha_ｉｊ方向移動.vss}'
    for icon, start, end in [('ha_i_j_VertexMove.png', 2466, 3121), ('ha_i_j_VertexMove@2x.png', 3245, 3769)]:
        assert wrapper[start:end] == (ROOT / 'resources/ha_ij_vertex_move/Images' / icon).read_bytes()
    with zipfile.ZipFile(io.BytesIO(files['ha_ij_direction.vwr'])) as resource:
        assert resource.testzip() is None
        for direction in ('Up', 'Down', 'Left', 'Right'):
            for suffix in ('', '@2x'):
                assert f'Images/ha_{direction}Arrow{suffix}.png' in resource.namelist()
    runtime = files['ha_VSFunctions.vlb']
    assert runtime[:2] == b'MZ'
    pe = struct.unpack_from('<I', runtime, 60)[0]
    assert runtime[pe:pe+4] == b'PE\0\0'
    assert struct.unpack_from('<H', runtime, pe+4)[0] == 0x8664
    assert b'ha_GetArrowKey' in runtime
    assert VERSION in files['README.md'].decode('utf-8')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--verify-only', action='store_true')
    args = parser.parse_args()
    package = ROOT / 'plugins' / PACKAGE
    files = {p.relative_to(package).as_posix(): p.read_bytes() for p in package.rglob('*') if p.is_file()}
    validate(files)
    archive = ROOT / 'dist' / f'{PACKAGE}-{VERSION}-vw2026-windows-x64.zip'
    if not args.verify_only:
        # Fixed metadata yields identical archives from identical contents.
        buffer = io.BytesIO()
        with zipfile.ZipFile(buffer, 'w', zipfile.ZIP_DEFLATED) as output:
            for name, data in sorted(files.items()):
                info = zipfile.ZipInfo(PACKAGE + '/' + name, (2026, 1, 1, 0, 0, 0))
                info.compress_type = zipfile.ZIP_DEFLATED
                info.create_system = 3
                info.external_attr = 0o100644 << 16
                output.writestr(info, data)
        data = buffer.getvalue()
        if archive.exists() and archive.read_bytes() != data:
            raise SystemExit('Refusing to replace a different archive; use a new candidate version.')
        archive.parent.mkdir(exist_ok=True)
        archive.write_bytes(data)
        Path(str(archive) + '.sha256').write_text(digest(data) + '  ' + archive.name + '\n', encoding='ascii')
    with zipfile.ZipFile(archive) as output:
        assert output.testzip() is None
        assert len(output.namelist()) == len(EXPECTED)
        assert set(output.namelist()) == {PACKAGE + '/' + n for n in EXPECTED}
        contents = {n: output.read(PACKAGE + '/' + n) for n in EXPECTED}
        validate(contents)
        assert contents == files
    value = digest(archive.read_bytes())
    assert Path(str(archive) + '.sha256').read_text(encoding='ascii') == value + '  ' + archive.name + '\n'
    print('PASS: manifest, INCLUDE, VST, paths, images, runtime, ZIP CRC and SHA-256')
    print(archive)
    print('SHA-256:', value)


if __name__ == '__main__':
    main()
