Summary:	PMU Plugin for Gkrellm 2.0
Summary(pl.UTF-8):   Plugin PMU dla Gkrellm 2.0
Name:		gkrellm-pmu
Version:	2.5
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/gkrellm-pmu/%{name}-%{version}.tar.gz
# Source0-md5:	a1a314e816994d1e2e1e3858a0a695d3
URL:		http://pbbuttons.berlios.de/projects/gkrellm-pmu/index.html
BuildRequires:	autoconf
BuildRequires:	gkrellm-devel >= 2.0
Requires:	gkrellm >= 2.0
ExclusiveArch:	ppc
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GKrellm-PMU creates a battery display for Apple Powerbook without
using APM frontends, which tend to be less verbose.

%description -l pl.UTF-8
GKrellm-PMU pokazuje stan baterii dla notebooków Apple Powerbook bez
użycia podsystemu APM, który jest mało treściwy.

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
%doc ChangeLog README
%attr(755,root,root) %{_libdir}/gkrellm2/plugins/pmu.so
