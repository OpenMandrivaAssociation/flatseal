Name:           flatseal
Version:        2.0.2
Release:        1
Summary:        Manage Flatpak permissions
License:        GPL-3.0-or-later
URL:            https://github.com/tchx84/flatseal
Source0:        %{url}/archive/v%{version}/Flatseal-%{version}.tar.gz

BuildRequires:  appstream-util
BuildRequires:  meson
BuildRequires:  desktop-file-utils
BuildRequires:  pkgconfig
BuildRequires:  gjs
BuildRequires:  pkgconfig(gjs-1.0)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:  pkgconfig(webkitgtk-6.0)
BuildArch:      noarch

%description
Flatseal is a graphical utility to review and modify permissions from your Flatpak applications.

%lang_package

%prep
%autosetup -n Flatseal-%{version} -p1

%build
%meson
%meson_build

%install
%meson_install
%find_lang %{name}

%files -f %{name}.lang
%license COPYING
%doc README.md CHANGELOG.md DOCUMENTATION.md
%{_bindir}/com.github.tchx84.Flatseal
%{_datadir}/appdata/com.github.tchx84.Flatseal.appdata.xml
%{_datadir}/glib-2.0/schemas/com.github.tchx84.Flatseal.gschema.xml
%{_datadir}/applications/com.github.tchx84.Flatseal.desktop
%{_datadir}/%{name}/
%{_datadir}/%{name}/com.github.tchx84.Flatseal.data.gresource
%{_datadir}/%{name}/com.github.tchx84.Flatseal.src.gresource
%{_datadir}/icons/hicolor/*/*/*.svg
