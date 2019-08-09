%global commit 34dab072f6ff5d13755b81aa79e71706b4b4d358
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           vlmc
Version:        0.2.0
Release:        0.16.git%{shortcommit}%{?dist}
Summary:        VideoLAN Movie Creator

License:        GPLv2+
URL:            https://www.videolan.org/vlmc/
Source0:        https://code.videolan.org/videolan/vlmc/repository/archive.tar.gz?ref=%{commit}#/%{name}-%{shortcommit}.tar.gz
Patch1:         vlmc-gcc47.patch

BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  hostname
BuildRequires:  libtool

BuildRequires:  pkgconfig(frei0r)
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5Quick)
BuildRequires:  pkgconfig(libvlc)
BuildRequires:  pkgconfig(libvlcpp)
BuildRequires:  pkgconfig(medialibrary)
BuildRequires:  pkgconfig(mlt-framework)


Requires:  frei0r-plugins
Requires:  mlt-freeworld >= 6.3


%description
VideoLAN Movie Creator is a non-linear editing software for video creation based on libVLC

%prep
%autosetup -p1 -n vlmc-%{commit}-%{commit}
./bootstrap


%build
%configure

%make_build V=1


%install
%make_install

mkdir -p %{buildroot}%{_datadir}/pixmaps
install -pm 0644 share/vlmc.png \
  %{buildroot}%{_datadir}/pixmaps

mkdir -p %{buildroot}%{_mandir}/man1
install -pm 0644 doc/vlmc.1 \
  %{buildroot}%{_mandir}/man1

desktop-file-install share/vlmc.desktop \
  %{buildroot}%{_datadir}/applications/vlmc.desktop


%files
%doc AUTHORS NEWS README.md TRANSLATORS
%license COPYING
%{_bindir}/vlmc
%{_mandir}/man1/vlmc.1.*
%{_datadir}/applications/vlmc.desktop
%{_datadir}/pixmaps/vlmc.png


%changelog
* Fri Aug 09 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.2.0-0.16.git34dab07
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Mar 05 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.2.0-0.15.git34dab07
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Aug 19 2018 Leigh Scott <leigh123linux@googlemail.com> - 0.2.0-0.14.git34dab07
- Rebuilt for Fedora 29 Mass Rebuild binutils issue

* Fri Jul 27 2018 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.2.0-0.13.git34dab07
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Mar 08 2018 Nicolas Chauvet <kwizart@gmail.com> - 0.2.0-0.12.git34dab07
- Rebase to gitlab source URL

* Thu Mar 08 2018 Sérgio Basto <sergio@serjux.com> - 0.2.0-0.11.git20170812
- Update to git20170812
- Move to autotools
- Add some new dependencies
- Spec clean up and add license tag

* Thu Mar 01 2018 RPM Fusion Release Engineering <leigh123linux@googlemail.com> - 0.2.0-0.10.git20120408
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild
* Thu Aug 31 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 0.2.0-0.9.git20120408
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Mar 20 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 0.2.0-0.8.git20120408
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Mar 03 2013 Nicolas Chauvet <kwizart@gmail.com> - 0.2.0-0.7.git20120408
- Mass rebuilt for Fedora 19 Features

* Sun Apr 08 2012 Nicolas Chauvet <kwizart@gmail.com> - 0.2.0-0.6.git20120408
- Update to 20120408 snapshot

* Fri Mar 09 2012 Nicolas Chauvet <kwizart@gmail.com> - 0.2.0-0.5.git991cfe4
- Update to 991cfe4

* Sun Jan 01 2012 Nicolas Chauvet <kwizart@gmail.com> - 0.2.0-0.4.gitbf8417f
- Update to today's git

* Mon Oct 17 2011 Nicolas Chauvet <kwizart@gmail.com> - 0.2.0-0.3.gitfbbb86f
- Update to current git

* Sun Jan 09 2011 Nicolas Chauvet <kwizart@gmail.com> - 0.2.0-0.2.git25a398b
- Update to 20110109git

* Tue Dec 14 2010 Nicolas Chauvet <kwizart@gmail.com> - 0.2.0-0.1.git13c4dbc
- Bump snapshot to pre 0.2.0

* Sat Apr 17 2010 Nicolas Chauvet <kwizart@fedoraproject.org> - 0.1.1-0.1
- Initial Spec file

