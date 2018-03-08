%global date 20170812

Name:           vlmc
Version:        0.2.0
Release:        0.11.git%{date}%{?dist}
Summary:        VideoLAN Movie Creator

Group:          Applications/Multimedia
License:        GPLv2+
URL:            http://trac.videolan.org/vlmc
Source0:        vlmc-%{date}.tar.bz2
Source9:        vlmc-snapshot.sh
Patch1:         vlmc-gcc47.patch

BuildRequires:  autoconf automake libtool
BuildRequires:  vlc-devel >= 3.0
BuildRequires:  libvlcpp-devel
BuildRequires:  medialibrary-devel
BuildRequires:  mlt-devel
BuildRequires:  frei0r-devel
BuildRequires:  qt5-devel >= 4.5.1
BuildRequires:  cmake >= 2.6.0
BuildRequires:  desktop-file-utils
BuildRequires:  /usr/bin/hostname
Requires:  frei0r-plugins

%description
VideoLAN Movie Creator is a non-linear editing software for video creation based on libVLC

%prep
%setup -q -n vlmc-%{date}
%patch1 -p1 -b .gcc47


%build
./bootstrap
./configure --help
%configure
%make_build VERBOSE=1


%install
%make_install

#rm -rf $RPM_BUILD_ROOT%{_datadir}/doc

# below is the desktop file and icon stuff.
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
desktop-file-install --dir $RPM_BUILD_ROOT%{_datadir}/applications \
  share/vlmc.desktop

mkdir -p $RPM_BUILD_ROOT%{_datadir}/pixmaps
install -p -m 644 share/vlmc.png \
  $RPM_BUILD_ROOT%{_datadir}/pixmaps

mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1
install -p -m 644 doc/vlmc.1 \
  $RPM_BUILD_ROOT%{_mandir}/man1

desktop-file-validate \
  $RPM_BUILD_ROOT%{_datadir}/applications/vlmc.desktop


%files
%doc AUTHORS NEWS README.md TRANSLATORS
%license COPYING
%{_bindir}/vlmc
%{_mandir}/man1/vlmc.1.*
%{_datadir}/applications/vlmc.desktop
%{_datadir}/pixmaps/vlmc.png


%changelog
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

