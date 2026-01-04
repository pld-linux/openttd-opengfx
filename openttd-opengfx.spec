Summary:	Open Source graphics base set for OpenTTD
Summary(pl.UTF-8):	Otwarty zestaw grafiki dla OpenTTD
Name:		openttd-opengfx
Version:	8.0
Release:	1
License:	GPL v2+
Group:		Applications/Games
Source0:	https://github.com/OpenTTD/OpenGFX/archive/refs/tags/%{version}/opengfx-%{version}-source.tar.gz
# Source0-md5:	7550ddfd319dd76f0899636cd508164c
URL:		http://wiki.openttd.org/Graphics_Replacement
BuildRequires:	grfcodec >= 5.0.0
BuildRequires:	nml >= 0.5.0
BuildRequires:	sed >= 4.0
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildConflicts:	gimp
Requires:	openttd-data >= 1.2
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
OpenGFX is an open source graphics base set for OpenTTD which can
completely replace the TTD base set. The main goal of OpenGFX
therefore is to provide a set of free base graphics which make it
possible to play OpenTTD without requiring the (copyrighted) files
from the TTD CD.

%description -l pl.UTF-8
OpenGFX to otwarty zestaw grafiki dla gry OpenTTD, który całkowicie
zastępuje zestaw podstawowy TTD. Głównym celem OpenGFX jest
dostarczenie darmowej grafiki, która umożliwii grę w OpenTTD bez
konieczności posiadania oryginalnych plików z gry TTD, strzeżonych
prawami autorskimi.

%prep
%setup -q -n OpenGFX-%{version}

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%define ogfxdir %{_datadir}/openttd/baseset/opengfx-%{version}
%{__make} install \
	INSTALL_DIR="$RPM_BUILD_ROOT%{ogfxdir}" \
	DESTDIR="$RPM_BUILD_ROOT"

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc changelog.txt README.md
%dir %{_datadir}/openttd/baseset/opengfx-%{version}
%{_datadir}/openttd/baseset/opengfx-%{version}/opengfx.obg
%{_datadir}/openttd/baseset/opengfx-%{version}/*.grf
%{_datadir}/openttd/baseset/opengfx-%{version}/*.txt
