# ref: dhd/droid-hal-device.inc

%define device rolex
%define vendor xiaomi

%define vendor_pretty Xiaomi
%define device_pretty Redmi 4A

%define installable_zip 1
%define droid_target_aarch64 1
%define android_version_major 7

%define android_config \
  #define WANT_ADRENO_QUIRKS 1 \
%{nil}

%define makefstab_skip_entries /dev/cpuctl /dev/bfqio /dev/stune /oem

%define straggler_files \
    /init.qcom.sh \
    /init.qcom.usb.sh \
    /bugreports \
    /d \
    /cache \
    /file_contexts.bin \
    /property_contexts \
    /seapp_contexts \
    /sdcard \
    /selinux_version \
    /service_contexts \
    /vendor \
    /charger \
    /sepolicy \
    /init.baseband.sh \
    /init.class_main.sh \
    /init.mdm.sh \
    /init.qcom.class_core.sh \
    /init.qcom.early_boot.sh \
    /init.qcom.sensors.sh \
    /init.qcom.syspart_fixup.sh \
%{nil}

%include rpm/dhd/droid-hal-device.inc
