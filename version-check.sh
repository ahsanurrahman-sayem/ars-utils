#!/bin/bash
#!/bin/ash
#!/bin/zsh

# Read the version from pyproject.toml
VERSION=$(python -c "import toml; print(toml.load('pyproject.toml')['project']['version'])")

# Check if the tag exists locally
if git rev-parse "v$VERSION" >/dev/null 2>&1; then
    echo "✅ Local tag v$VERSION already exists."
else
    echo "Creating local tag v$VERSION..."
    git tag v$VERSION
fi

# Check if the tag exists on GitHub
if git ls-remote --tags origin | grep -q "refs/tags/v$VERSION"; then
    echo "✅ Remote tag v$VERSION already exists."
else
    echo "Pushing tag v$VERSION to GitHub..."
    git push origin v$VERSION
fi