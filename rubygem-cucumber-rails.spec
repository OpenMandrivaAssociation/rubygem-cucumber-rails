%define oname cucumber-rails

Name:       rubygem-%{oname}
Version:    0.3.2
Release:    %mkrel 1
Summary:    Cucumber Generators and Runtime for Rails
Group:      Development/Ruby
License:    MIT
URL:        http://github.com/aslakhellesoy/cucumber-rails
Source0:    http://rubygems.org/gems/%{oname}-%{version}.gem
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-root
Requires:   rubygems
Suggests:   rubygem(aruba) >= 0.1.9
BuildRequires: rubygems
BuildArch:  noarch
Provides:   rubygem(%{oname}) = %{version}

%description
Cucumber Generators and Runtime for Rails


%prep

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{ruby_gemdir}
gem install --local --install-dir %{buildroot}%{ruby_gemdir} \
            --force --rdoc %{SOURCE0}

find %{buildroot}%{ruby_gemdir}/gems/%{oname}-%{version}/ -name ".gitignore" -exec rm -f {} \;
chmod -x %{buildroot}%{ruby_gemdir}/gems/%{oname}-%{version}/History.txt
%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root, -)
%dir %{ruby_gemdir}/gems/%{oname}-%{version}/
%{ruby_gemdir}/gems/%{oname}-%{version}/dev_tasks/
%{ruby_gemdir}/gems/%{oname}-%{version}/features/
%{ruby_gemdir}/gems/%{oname}-%{version}/generators/
%{ruby_gemdir}/gems/%{oname}-%{version}/lib/
%{ruby_gemdir}/gems/%{oname}-%{version}/spec/
%{ruby_gemdir}/gems/%{oname}-%{version}/templates/
%doc %{ruby_gemdir}/doc/%{oname}-%{version}
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/HACKING.rdoc
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/History.txt
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/LICENSE
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/Rakefile
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/README.rdoc
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/VERSION
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/%{oname}.gemspec
%{ruby_gemdir}/cache/%{oname}-%{version}.gem
%{ruby_gemdir}/specifications/%{oname}-%{version}.gemspec


%changelog
* Mon Dec 20 2010 Rémy Clouard <shikamaru@mandriva.org> 0.3.2-1mdv2011.0
+ Revision: 623461
- import rubygem-cucumber-rails

