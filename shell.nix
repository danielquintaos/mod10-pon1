{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell {
  buildInputs = [
    pkgs.python39Full
    pkgs.python39Packages.pip
    pkgs.python39Packages.virtualenv
  ];

  shellHook = ''
    if [ ! -d ".venv" ]; then
      echo "Creating a virtual environment..."
      virtualenv .venv
    fi

    echo "Activating virtual environment..."
    source .venv/bin/activate

    if [ ! -f "requirements.txt" ]; then
      echo "requirements.txt not found."
    else
      echo "Installing Python dependencies..."
      pip install -r requirements.txt
    fi
  '';
}
