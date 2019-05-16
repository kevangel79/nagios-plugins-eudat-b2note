Name:		nagios-plugins-eudat-b2note
Version:	1.0
Release:	2%{?dist}
Summary:	Nagios Eudat b2note
License:	GPLv3+
Packager:	Themis Zamani <themiszamani@gmail.com>

Source:		%{name}-%{version}.tar.gz
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}
AutoReqProv: no

%description
Nagios probes to check functionality of cas server

%prep
%setup -q

%define _unpackaged_files_terminate_build 0 

%install

install -d %{buildroot}/%{_libexecdir}/argo-monitoring/probes/eudat-b2note
install -d %{buildroot}/%{_sysconfdir}/nagios/plugins/eudat-b2note
install -m 755 check_b2note.sh %{buildroot}/%{_libexecdir}/argo-monitoring/probes/eudat-b2note/check_b2note.sh

%files
%dir /%{_libexecdir}/argo-monitoring
%dir /%{_libexecdir}/argo-monitoring/probes/
%dir /%{_libexecdir}/argo-monitoring/probes/eudat-b2note

%attr(0755,root,root) /%{_libexecdir}/argo-monitoring/probes/eudat-b2note/check_b2note.sh

%changelog
* Thu May 16 2019 Themis Zamani <themiszamani@gmail.com> - 1.0-2
- New version
* Tue Jul 2 2018 Themis Zamani <themiszamani@gmail.com> - 1.0-1
- Initial version of the package. 



