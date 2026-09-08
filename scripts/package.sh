#!/usr/bin/env bash
# Package each skill into its own zip, ready to upload to Claude as a custom skill.
# Usage: bash scripts/package.sh
# Output: dist/<skill-name>.zip, plus dist/girard-deal-skills.zip containing all six.

set -euo pipefail
cd "$(dirname "$0")/.."

python3 scripts/validate_skills.py

rm -rf dist && mkdir -p dist

for dir in skills/*/; do
  name="$(basename "$dir")"
  (cd skills && zip -qr "../dist/${name}.zip" "$name" -x '*.DS_Store')
  echo "packaged dist/${name}.zip"
done

(cd skills && zip -qr ../dist/girard-deal-skills.zip . -x '*.DS_Store')
echo "packaged dist/girard-deal-skills.zip"
