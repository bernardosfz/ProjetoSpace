#pip install cx_freeze
import cx_Freeze
executables =[
    cx_Freeze.Executable(script="main.py", icon="icone.ico")
]
cx_Freeze.setup(
    name = "Space Discovery",
    options={
        "build_exe":{
            "packages":["pygame"],
            "include_files":["assets"]
        }
    }, executables = executables
)

#py setup.py build
#py setup.py bdist_msi