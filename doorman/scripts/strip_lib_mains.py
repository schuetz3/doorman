Import("env")
import os

# libesplog and libmqttdisco ship stray src/main.cpp sketches that collide
# with the project's setup()/loop() at link time. Remove them before build.
STRAY_FILES = [
    os.path.join(env.subst("$PROJECT_LIBDEPS_DIR"), env.subst("$PIOENV"), "libesplog", "src", "main.cpp"),
    os.path.join(env.subst("$PROJECT_LIBDEPS_DIR"), env.subst("$PIOENV"), "libmqttdisco", "src", "main.cpp"),
]

for path in STRAY_FILES:
    if os.path.isfile(path):
        os.remove(path)
        print(f"strip_lib_mains: removed {path}")
