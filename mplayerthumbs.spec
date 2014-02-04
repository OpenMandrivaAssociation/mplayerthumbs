Name:		mplayerthumbs
Version:	4.12.2
Release:	1
Epoch:		3
Summary:	Video thumbnail generator for KDE4 file managers
Group:		Graphical desktop/KDE
License:	GPLv2
URL:		https://projects.kde.org/projects/kde/kdemultimedia/mplayerthumbs
Source:		ftp://ftp.kde.org/pub/kde/stable/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	kdelibs4-devel
Requires:	kdebase4-runtime

%description
MPlayerThumbs is a video thumbnail generator for KDE file managers
(Konqueror, Dolphin, ...), now available also for KDE 4.
It needs mplayer (of course) to generate thumbnails, and it contains
no linking to any library, so in a x86_64 system you can freely use the
32bit mplayer binary with win32codecs by configuring the application
launching the mplayerthumbsconfig helper application.
It catches a random frame from 15% to 70%, checking also how contrasted
is the image, and dropping bad frames.

%files
%{_kde_bindir}/mplayerthumbsconfig
%{_kde_libdir}/kde4/videopreview.so
%{_kde_appsdir}/videothumbnail
%{_kde_datadir}/config.kcfg/mplayerthumbs.kcfg
%{_kde_services}/videopreview.desktop

#------------------------------------------------------------------------------

%prep
%setup -q

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

%changelog
* Tue Feb 04 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 3:4.12.2-1
- New version 4.12.2

* Tue Jan 14 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 3:4.12.1-1
- New version 4.12.1

* Wed Dec 04 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 3:4.11.4-1
- New version 4.11.4

* Wed Nov 06 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 3:4.11.3-1
- New version 4.11.3

* Wed Oct 02 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 3:4.11.2-1
- New version 4.11.2

* Tue Sep 03 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 3:4.11.1-1
- New version 4.11.1

* Wed Aug 14 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 3:4.11.0-1
- New version 4.11.0

* Wed Jul 03 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 3:4.10.5-1
- New version 4.10.5

* Wed Jun 05 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 3:4.10.4-1
- New version 4.10.4

* Tue May 07 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 3:4.10.3-1
- New version 4.10.3

* Wed Apr 03 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 3:4.10.2-1
- New version 4.10.2

* Sat Mar 09 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 3:4.10.1-1
- New version 4.10.1

* Thu Feb 07 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 3:4.10.0-1
- New version 4.10.0

* Wed Dec 05 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 3:4.9.4-1
- New version 4.9.4

* Wed Nov 07 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 3:4.9.3-1
- New version 4.9.3

* Thu Oct 04 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 3:4.9.2-1
- New version 4.9.2

* Sat Sep 08 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 3:4.9.1-1
- New version 4.9.1

* Tue Aug 14 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 3:4.9.0-1
- New version 4.9.0

* Thu Jul 12 2012 Andrey Bondrov <abondrov@mandriva.org> 3:4.8.97-1
+ Revision: 808947
- imported package mplayerthumbs

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

* Wed Oct 29 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 1.1-1mdv2009.1
+ Revision: 298155
- Fix BuildRequires
- import mplayerthumbs

