{ }:

let
    pkgs = import <nixpkgs> { };
in

with pkgs;

buildEnv {
  name = "buildout-deco-env";
  paths = [
    python27
    python27Packages.virtualenv
    python27Packages.recursivePthLoader
    python27Packages."zc.buildout-1.7.1"
    python27Packages."Plone-4.3.2"
  ] ++ lib.attrValues python27.modules;
}
