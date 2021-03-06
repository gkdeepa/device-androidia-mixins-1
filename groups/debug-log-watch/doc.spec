=== Overview

log watch is used to classify different kind of logs.

--- deps

    - sepolicy
    - debug-crashlogd


==== Options

--- true
this option will enable logwatch in android build

    --- code dir
        - device/intel/sepolicy/log-watch
        - vendor/intel/tools/log_capture/log-watch

    --- extra files
        - init.log-watch.rc: "Debug specific init scripts"
        - log-watch-kmsg.cfg: "Log Watch /dev/kmsg configuration"

--- false
this option will disable logwatch in android build

--- default
when not explicitly selected in mixin spec file, the default option will be used.
