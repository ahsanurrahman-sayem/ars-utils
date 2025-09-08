#!/bin/bash
set -e

# 1️⃣ Read version from pyproject.toml
VERSION=$(python -c "import toml; print(toml.load('pyproject.toml')['project']['version'])")
TAG="v$VERSION"
echo "Version from pyproject.toml: $VERSION"

# 2️⃣ Commit any pending changes (optional)
if ! git diff-index --quiet HEAD --; then
    echo "Committing pending changes..."
    git add .
    git commit -m "Update code for version $VERSION"
else
    echo "No changes to commit."
fi

# 3️⃣ Create or update the tag locally
if git rev-parse "$TAG" >/dev/null 2>&1; then
    echo "Tag $TAG already exists locally. Recreating it..."
    git tag -f $TAG
else
    echo "Creating tag $TAG..."
    git tag $TAG
fi

# 4️⃣ Push commits and tag to GitHub
echo "Pushing commits and tag $TAG to origin..."
git push origin HEAD
git push origin $TAG --force

echo "✅ Done! Tag $TAG pushed successfully."