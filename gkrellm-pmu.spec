Summary:	PMU Plugin for Gkrellm 2.0
Summary(pl):	Plugin PMU dla Gkrellm 2.0
Name:		gkrellm-pmu
Version:	2.3
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	0ad6b7e36da369be0df76310e0b690d9
URL:		http://www.cymes.de/members/joker/projects/gkrellm-pmu/gkrellm-pmu.html
BuildRequires:	autoconf
BuildRequires:	gkrellm-devel >= 2.0
Requires:	gkrellm >= 2.0
ExclusiveArch:	ppc
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GKrellm-PMU creates a battery display for Apple Powerbook without
using APM frontends, which tend to be less verbose.

%description -l pl
GKrellm-PMU pokazuje stan baterii dla notebooków Apple Powerbook bez
u¿ycia podsystemu APM, który jest ma³o tre¶ciwy.

%prep
%setup -q

%build
%{__autoconf}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/gkrellm2/plugins

install src/pmu.so $RPM_BUILD_ROOT%{_libdir}/gkrellm2/plugins

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README Theming
%attr(755,root,root) %{_libdir}/gkrellm2/plugins/pmu.so
