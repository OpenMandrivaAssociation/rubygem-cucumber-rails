%define oname cucumber-rails

Name:       rubygem-%{oname}
Version:    1.4.1
Release:    1
Summary:    Cucumber Generators and Runtime for Rails
Group:      Development/Ruby
License:    MIT
URL:        http://github.com/aslakhellesoy/cucumber-rails
Source0:    http://rubygems.org/gems/cucumber-rails-1.4.1.gem
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
mkdir -p %{buildroot}%{ruby_gemdir}
gem install --local --install-dir %{buildroot}%{ruby_gemdir} \
            --force --rdoc %{SOURCE0}

find %{buildroot}%{ruby_gemdir}/gems/%{oname}-%{version}/ -name ".gitignore" -exec rm -f {} \;
chmod -x %{buildroot}%{ruby_gemdir}/gems/%{oname}-%{version}/History.txt
%clean

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
