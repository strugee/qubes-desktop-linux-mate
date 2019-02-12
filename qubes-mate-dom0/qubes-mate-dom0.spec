# This is a meta package that makes installing all MATE components easy

%if 0%{?qubes_builder}
%define _sourcedir %(pwd)/qubes-mate-dom0
%define qubes_mate_dom0_version %(cat version)
%endif
%{!?version: %define version %(cat version)}


Name:Requires:  qubes-mate-dom0
Summary: Metapackage for installing all MATE components needed for Qubes Dom0
Version: %{qubes_mate_dom0_version}
Release: 3%{?dist}

License: GPL2
URL: http://qubes-os.org

BuildArch: noarch

Requires: qubes-desktop-linux-common
Requires: marco
Requires: mate-applets
Requires: mate-backgrounds
Requires: mate-calc
Requires: mate-control-center
Requires: mate-desktop
Requires: mate-dictionary
Requires: mate-disk-usage-analyzer
Requires: mate-icon-theme
Requires: mate-media
Requires: mate-menus
Requires: mate-menus-preferences-category-menu
Requires: mate-notification-daemon
Requires: mate-panel
Requires: mate-polkit
Requires: mate-power-manager
Requires: mate-screensaver
Requires: mate-screenshot
Requires: mate-search-tool
Requires: mate-session-manager
Requires: mate-settings-daemon
Requires: mate-system-log
Requires: mate-system-monitor
Requires: mate-terminal
Requires: mate-themes
Requires: mate-user-admin
Requires: mate-user-guide

# other 3rd party packages that are useful in Dom0...

# This is for people who don't use NetVM (i.e. don't have VT-d hardware)
# This should be left to the user IMO
#Requires: network-manager-applet
#Requires: nm-connection-editor

# Qubes-customized menus
Requires: qubes-menus

%description
%{summary}.

%install

%files
%defattr (-,root,root,-)

%changelog
* Mon Feb 11 2019 AJ Jordan <alex@strugee.net>
- Initial release (based on the Qubes KDE spec and the Fedora 28 MATE desktop group)
