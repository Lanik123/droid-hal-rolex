# ref: dhd/droid-hal-device.inc

%define device rolex
%define vendor xiaomi

%define vendor_pretty Xiaomi
%define device_pretty Redmi 4A

%define installable_zip 1
%define droid_target_aarch64 1

%define android_config \
  #define WANT_ADRENO_QUIRKS 1 \
%{nil}

%include rpm/dhd/droid-hal-device.inc
