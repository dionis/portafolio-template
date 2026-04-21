python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
rm -rf public
reflex init
reflex export --frontend-only
unzip frontend.zip -d public
rm -f frontend.zip

# Remove the backend connection error overlay from the static frontend.
# Reflex always includes DefaultOverlayComponents which tries to connect via
# WebSocket and shows a "Cannot connect to server" toast on static hosting.
find public -name '*.js' -exec sed -i 's/jsx(DefaultOverlayComponents,{})/null/g' {} +

deactivate