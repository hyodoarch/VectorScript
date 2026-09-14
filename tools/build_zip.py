from pathlib import Path
import hashlib
import zipfile

root = Path(__file__).resolve().parents[1]
package = root / 'plugins/ha_ij_direction'
dist = root / 'dist'
dist.mkdir(exist_ok=True)
archive = dist / 'ha_ij_direction-v0.1.0-vw2026-windows-x64.zip'
with zipfile.ZipFile(archive, 'w', zipfile.ZIP_DEFLATED) as output:
    for path in sorted(package.rglob('*')):
        if path.is_file():
            output.write(path, path.relative_to(package.parent).as_posix())
digest = hashlib.sha256(archive.read_bytes()).hexdigest()
(dist / (archive.name + '.sha256')).write_text(digest + '  ' + archive.name + '\n', encoding='ascii')
print(archive)
print('SHA-256:', digest)
