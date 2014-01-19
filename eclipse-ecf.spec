%{?_javapackages_macros:%_javapackages_macros}
%{?scl:%scl_package eclipse-ecf}
%{!?scl:%global pkg_name %{name}}

%global tag 	R-Release_HEAD-sdk_feature-113_2013-06-05_17-43-35
%global contextQualifier v20130605-1748

%define __requires_exclude osgi*

Name:           %{?scl_prefix}eclipse-ecf
Version:        3.6.1
Release:        1.1%{?dist}
Summary:        Eclipse Communication Framework

License:        EPL
URL:            http://www.eclipse.org/ecf/
Source0:        http://git.eclipse.org/c/ecf/org.eclipse.ecf.git/snapshot/org.eclipse.ecf-%{tag}.tar.bz2

BuildRequires:  java-devel >= 1.7.0 
BuildRequires:  jpackage-utils
BuildRequires:  eclipse-pde >= 4.2.0-5
BuildRequires:	httpcomponents-client
BuildRequires:	httpcomponents-core
BuildRequires:	jakarta-commons-httpclient
BuildRequires:	apache-commons-logging

BuildArch:      noarch

%description
ECF is a framework for building distributed servers, applications,
 and tools. It provides a modular implementation of the OSGi 4.2
 Remote Services standard, along with support for REST-based and
 SOAP-based remote services, and asynchronous messaging for remote services. 

%package core
Summary:   ECF core bundles

Requires:       java >= 1:1.7.0
Requires:       jpackage-utils
%{?scl:Requires: %scl_runtime}

%description core
ECF bundles required by eclipse-platform.

%prep
%setup -q -n org.eclipse.ecf-%{tag}

#get just the bits we need
mkdir -p ecf/plugins
mkdir -p ecf/features

cp -r releng/features/org.eclipse.ecf.filetransfer{,.httpclient4}.feature \
    ecf/features

cp -r framework/bundles/org.eclipse.ecf ecf/plugins
cp -r framework/bundles/org.eclipse.ecf.identity ecf/plugins
cp -r framework/bundles/org.eclipse.ecf.ssl ecf/plugins
cp -r framework/bundles/org.eclipse.ecf.filetransfer ecf/plugins
cp -r providers/bundles/org.eclipse.ecf.provider.filetransfer ecf/plugins
cp -r providers/bundles/org.eclipse.ecf.provider.filetransfer.ssl ecf/plugins
cp -r providers/bundles/org.eclipse.ecf.provider.filetransfer.httpclient4 ecf/plugins
cp -r providers/bundles/org.eclipse.ecf.provider.filetransfer.httpclient4.ssl ecf/plugins

rm -rf `ls | grep -v "ecf"`

find . -type f -name "*.jar" -exec rm {} \;

mkdir -p deps
pushd deps
	ln -s /usr/share/java/httpcomponents/httpclient.jar
	ln -s /usr/share/java/httpcomponents/httpcore.jar
	ln -s /usr/share/java/commons-httpclient.jar
	ln -s /usr/share/java/commons-logging.jar
popd

sed -i -e 's/4.1.0/[4.1.0,5.0.0)/g' ecf/plugins/org.eclipse.ecf.provider.filetransfer.httpclient4/META-INF/MANIFEST.MF
sed -i -e 's#;bundle-version="1.1.1"##g' ecf/plugins/org.eclipse.ecf.provider.filetransfer.httpclient4/META-INF/MANIFEST.MF
sed -i -e 's#1.1.1#0.0.0#g' ecf/features/org.eclipse.ecf.filetransfer.httpclient4.feature/feature.xml 
sed -i -e 's#(Object) ((URIID) o)#((URIID) o)#g' ecf/plugins/org.eclipse.ecf.identity/src/org/eclipse/ecf/core/identity/URIID.java
sed -i -e '10i#org.apache.commons.logging,' ecf/plugins/org.eclipse.ecf.provider.filetransfer.httpclient4/META-INF/MANIFEST.MF
sed -i -e '10i#org.apache.commons.logging,' ecf/plugins/org.eclipse.ecf.provider.filetransfer/META-INF/MANIFEST.MF

%build
eclipse-pdebuild -f org.eclipse.ecf.filetransfer.feature -j "-DforceContextQualifier=%{contextQualifier}" -o `pwd`/deps
eclipse-pdebuild -f org.eclipse.ecf.filetransfer.httpclient4.feature -j "-DforceContextQualifier=%{contextQualifier}" -o `pwd`/deps 


%install
install -d -m 755 %{buildroot}%{_javadir}/ecf

unzip -q -n -d %{buildroot}%{_javadir}/ecf          build/rpmBuild/org.eclipse.ecf.filetransfer.feature.zip
unzip -q -n -d %{buildroot}%{_javadir}/ecf          build/rpmBuild/org.eclipse.ecf.filetransfer.httpclient4.feature.zip

pushd %{buildroot}%{_javadir}/ecf/eclipse/plugins/
rm -rf org.apache*
#remove timestamps from name to make symlinking easy
for f in \
org.eclipse.ecf.filetransfer \
org.eclipse.ecf.identity \
org.eclipse.ecf.provider.filetransfer.httpclient4.ssl \
org.eclipse.ecf.provider.filetransfer.httpclient4 \
org.eclipse.ecf.provider.filetransfer.ssl \
org.eclipse.ecf.provider.filetransfer \
org.eclipse.ecf.ssl \
org.eclipse.ecf ; do \
	mv ${f}_*.jar ${f}.jar
done
popd

%files core
%{_javadir}/ecf
%doc ecf/features/org.eclipse.ecf.filetransfer.feature/license.html
%doc ecf/features/org.eclipse.ecf.filetransfer.feature/about.html

%changelog
* Tue Sep 3 2013 Krzysztof Daniel <kdaniel@redhat.com> 3.6.1-1
- Update to latest upstream.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Jun 21 2013 Krzysztof Daniel <kdaniel@redhat.com> 3.6.0-2
- 974112: Remove versions and timestamps from ECF.

* Wed May 1 2013 Krzysztof Daniel <kdaniel@redhat.com> 3.6.0-1
- Update to latest upstream.

* Mon Apr 8 2013 Krzysztof Daniel <kdaniel@redhat.com> 3.5.7-0.6
- Rebuild with old commons logging.

* Mon Apr 8 2013 Krzysztof Daniel <kdaniel@redhat.com> 3.5.7-0.5
- Drop v3 httpclient.
- Make dependency to commons loggigng less strict.

* Wed Mar 20 2013 Krzysztof Daniel <kdaniel@redhat.com> 3.5.7-0.4
- Add direct dependency to jakarta-commons-httpclient.

* Wed Mar 20 2013 Krzysztof Daniel <kdaniel@redhat.com> 3.5.7-0.3
- Symlink deps against /usr/share/java/.

* Fri Mar 15 2013 Krzysztof Daniel <kdaniel@redhat.com> 3.5.7-0.2
- Explicitly build httpclient4 feature.

* Thu Mar 14 2013 Krzysztof Daniel <kdaniel@redhat.com> 3.5.7-0.1
- Update to latest upstream.
- Initial SCLization.

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.5.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Oct 8 2012 Krzysztof Daniel <kdaniel@redhat.com> 3.5.6-7
- Use __requires_exclude instead of __provides_exclude.

* Mon Oct 8 2012 Krzysztof Daniel <kdaniel@redhat.com> 3.5.6-6
- Try out __provides_exclude

* Mon Oct 8 2012 Krzysztof Daniel <kdaniel@redhat.com> 3.5.6-5
- Use new way of changing auto required dependencies.

* Fri Oct 5 2012 Krzysztof Daniel <kdaniel@redhat.com> 3.5.6-4
- Don't generate autorreuquire.

* Mon Aug 27 2012 Krzysztof Daniel <kdaniel@redhat.com> 3.5.6-3
- Don't duplicate org.apache* plugins
- Use context qualifier to avoid constant feature version changes.

* Wed Aug 8 2012 Krzysztof Daniel <kdaniel@redhat.com> 3.5.6-2
- Review issues fixed.

* Wed Aug 8 2012 Krzysztof Daniel <kdaniel@redhat.com> 3.5.6-1
- Initial packaging.
