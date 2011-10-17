%global gitsnapshot fbbb86f

Name:           vlmc
Version:        0.2.0
Release:        0.3.git%{gitsnapshot}%{?dist}
Summary:        VideoLAN Movie Creator

Group:          Applications/Multimedia
License:        GPLv2+
URL:            http://trac.videolan.org/vlmc
#Current snapshot at 20110109
#http://git.videolan.org/?p=vlmc.git;a=snapshot;h=25a398b4e84a81e1482f93957f55077f4842f59e;sf=tgz
Source0:        vlmc-%{gitsnapshot}.tar.gz
Patch0:         vlmc-13c4dbc-ldf.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  vlc-devel >= 1.1.4
BuildRequires:  frei0r-devel
BuildRequires:  qt-devel >= 4.5.1
BuildRequires:  cmake >= 2.6.0
BuildRequires:  desktop-file-utils
Requires:  frei0r-plugins

%description
VideoLAN Movie Creator is a non-linear editing software for video creation based on libVLC

%prep
%setup -q -n vlmc-%{gitsnapshot}
%patch0 -p1 -b .ldf


%build
mkdir -p build
pushd build
%cmake \
  -DVLMC_LIB_SUBDIR=%{_lib} \
  -DCMAKE_BUILD_TYPE=Release \
  ..

make VERBOSE=1 %{?_smp_mflags}
popd


%install
rm -rf $RPM_BUILD_ROOT
pushd build
make install DESTDIR=$RPM_BUILD_ROOT
popd

rm -rf $RPM_BUILD_ROOT%{_datadir}/doc

desktop-file-validate \
  $RPM_BUILD_ROOT%{_datadir}/applications/vlmc.desktop


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING NEWS README TRANSLATORS
%{_bindir}/vlmc
%{_mandir}/man1/vlmc.1.*
%{_datadir}/applications/vlmc.desktop
%{_datadir}/pixmaps/vlmc.png


%changelog
* Mon Oct 17 2011 Nicolas Chauvet <kwizart@gmail.com> - 0.2.0-0.3.gitfbbb86f
- Update to current git

* Sun Jan 09 2011 Nicolas Chauvet <kwizart@gmail.com> - 0.2.0-0.2.git25a398b
- Update to 20110109git

* Tue Dec 14 2010 Nicolas Chauvet <kwizart@gmail.com> - 0.2.0-0.1.git13c4dbc
- Bump snapshot to pre 0.2.0

* Sat Apr 17 2010 Nicolas Chauvet <kwizart@fedoraproject.org> - 0.1.1-0.1
- Initial Spec file

