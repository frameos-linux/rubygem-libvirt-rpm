# Generated from libvirt-0.0.1.dev.gem by gem2rpm -*- rpm-spec -*-
%define ruby_sitelib %(ruby -rrbconfig -e "puts Config::CONFIG['sitelibdir']")
%define gemdir %(ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define gemname libvirt
%define geminstdir %{gemdir}/gems/%{gemname}-%{version}

Summary: A ruby client library providing the raw interface to libvirt via FFI
Name: rubygem-%{gemname}
Version: 0.0.1.20101018
Release: 2%{?dist}
Group: Development/Languages
License: GPLv2+ or Ruby
URL: http://rubygems.org/gems/libvirt
Source0: %{gemname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires: rubygems
Requires: rubygem(ffi) >= 0.6.3
Requires: rubygem(builder) >= 2.1.2
Requires: rubygem(nokogiri) >= 1.4.1
BuildRequires: rubygems
BuildArch: noarch
Provides: rubygem(%{gemname}) = %{version}

%description
A ruby client library providing the raw interface to libvirt via FFI.


%prep

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{gemdir}
gem install --local --install-dir %{buildroot}%{gemdir} \
            --force --rdoc %{SOURCE0}

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root, -)
%{gemdir}/gems/%{gemname}-%{version}/
%doc %{gemdir}/doc/%{gemname}-%{version}
%{gemdir}/cache/%{gemname}-%{version}.gem
%{gemdir}/specifications/%{gemname}-%{version}.gemspec


%changelog
* Mon Oct 18 2010 : Sergio Rubio <rubiojr@frameos.org> - 0.0.1.20101018-2
- Fix install so check-buildroot does not complain

* Mon Oct 18 2010 : Sergio Rubio <rubiojr@frameos.org> - 0.0.1.dev-1
- Initial package
