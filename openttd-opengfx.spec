Summary:	Open Source graphics base set for OpenTTD
Summary(pl.UTF-8):	Otwarty zestaw grafiki dla OpenTTD
Name:		opengfx
Version:	0.2.3
Release:	1
License:	GPL v2+
Group:		Applications/Games
Source0:	http://bundles.openttdcoop.org/opengfx/releases/%{name}-%{version}-source.tar.gz
# Source0-md5:	5e530e70e4ed5f2b20cc8b739c633830
URL:		http://wiki.openttd.org/Graphics_Replacement
BuildRequires:	grfcodec >= r2245
BuildRequires:	nforenum >= r2281
BuildRequires:	openttd-data
BuildRequires:	sed >= 4.0
Requires:	openttd-data
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
%setup -q -n %{name}-%{version}-source
%{__sed} -i 's,$(INSTALL_DIR),$(DESTDIR)$(INSTALL_DIR),' scripts/Makefile.bundles

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	INSTALL_DIR="%{_datadir}/openttd/data" \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc docs/{changelog.txt,readme.txt}
%{_datadir}/openttd/data/opengfx-0.2.3.tar