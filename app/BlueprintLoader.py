import importlib
import os

class BlueprintLoader:
    def __init__(self):
        pass

    @staticmethod
    def discover_blueprints_by_pattern():
        package_blueprints = list()
        akselcore_packages = os.listdir('app')

        for package in akselcore_packages:
            if ".py" in package:
                continue
            if "." in package:
                continue
            if "__" in package:
                continue

            package = ".{}.blueprints".format(package)
            try:
                spec = importlib.util.find_spec(package, 'app')
                if spec is None:
                    continue
                else:
                    akselcore_module = importlib.util.module_from_spec(spec)
                    spec.loader.exec_module(akselcore_module)

                    package_attributes = dir(akselcore_module)
                    pmodules = [pm for pm in package_attributes if "_blueprint" in pm]
                    for pmodule in pmodules:
                        package_blueprints.append(getattr(akselcore_module, pmodule))
            except Exception as e:
                raise Exception(e)
                continue

        return package_blueprints
