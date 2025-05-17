{
  inputs = {
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = { self, nixpkgs, flake-utils }:
    flake-utils.lib.eachDefaultSystem
      (system: let
        pkgs = (import nixpkgs { inherit system; });
      in
        {
          devShell = with pkgs.python312Packages; buildPythonPackage rec {
            name = "proj4d";
            src = ./src;
            propagatedBuildInputs = with pkgs; [ libGL pygame-ce moderngl numpy numba ];
            LD_LIBRARY_PATH = pkgs.lib.makeLibraryPath propagatedBuildInputs;
          };
          formatter = pkgs.nixpkgs-fmt;
        }
      );
}
