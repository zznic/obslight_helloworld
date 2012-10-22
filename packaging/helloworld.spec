#
# spec file for package 
#
# Copyright (c) 2012 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the 
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9) 
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#

Name:           helloworld
Version:		1.0
Release:		0
License:		GPL v2
Summary:		A simple hello world program	
Group:			Eduction
Source:			%{name}-%{version}.tar.gz
#Patch:
#BuildRequires:
#PreReq:
#Provides:
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description

%prep
%setup -q

%build
make %{?_smp_mflags}

%install
mkdir -p $RPM_BUILD_ROOT/%{_bindir}
install -m 0755 helloworld $RPM_BUILD_ROOT/%{_bindir}

%clean
rm -rf "$RPM_BUILD_ROOT"

%post

%postun

%files
%defattr(-,root,root)
%{_bindir}/helloworld

#%doc ChangeLog README COPYING

%changelog

