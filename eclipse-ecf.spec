
%undefine _compress
%undefine _extension
%global _duplicate_files_terminate_build 0
%global _files_listed_twice_terminate_build 0
%global _unpackaged_files_terminate_build 0
%global _nonzero_exit_pkgcheck_terminate_build 0
%global _use_internal_dependency_generator 0
%global __find_requires /bin/sed -e 's/.*//'
%global __find_provides /bin/sed -e 's/.*//'

Name:		eclipse-ecf-core
Version:	3.6.1
Release:	1.0
License:	GPLv3+
Source0:	eclipse-ecf-core-3.6.1-1.0-omv2014.0.noarch.rpm

URL:		https://abf.rosalinux.ru/openmandriva/eclipse-ecf-core
BuildArch:	noarch
Summary:	eclipse-ecf-core bootstrap version
Requires:	javapackages-bootstrap
Requires:	java >= 1:1.7.0
Requires:	jpackage-utils
Requires:	osgi(org.apache.commons.logging)
Requires:	osgi(org.apache.httpcomponents.httpclient)
Requires:	osgi(org.eclipse.equinox.common)
Requires:	osgi(org.eclipse.equinox.registry)
Requires:	osgi(org.eclipse.osgi)
Provides:	eclipse-ecf-core = 3.6.1-1.0:2014.0
Provides:	osgi(org.eclipse.ecf) = 3.2.0
Provides:	osgi(org.eclipse.ecf.filetransfer) = 5.0.0
Provides:	osgi(org.eclipse.ecf.identity) = 3.2.0
Provides:	osgi(org.eclipse.ecf.provider.filetransfer) = 3.2.0
Provides:	osgi(org.eclipse.ecf.provider.filetransfer.httpclient4) = 1.0.300
Provides:	osgi(org.eclipse.ecf.provider.filetransfer.httpclient4.ssl) = 1.0.0
Provides:	osgi(org.eclipse.ecf.provider.filetransfer.ssl) = 1.0.0
Provides:	osgi(org.eclipse.ecf.ssl) = 1.1.0

%description
eclipse-ecf-core bootstrap version.

%files
/usr/share/doc/eclipse-ecf-core
/usr/share/doc/eclipse-ecf-core/about.html
/usr/share/doc/eclipse-ecf-core/license.html
/usr/share/java/ecf
/usr/share/java/ecf/eclipse
/usr/share/java/ecf/eclipse/features
/usr/share/java/ecf/eclipse/features/org.eclipse.ecf.filetransfer.feature_3.7.100.v20130605-1748
/usr/share/java/ecf/eclipse/features/org.eclipse.ecf.filetransfer.feature_3.7.100.v20130605-1748/about.html
/usr/share/java/ecf/eclipse/features/org.eclipse.ecf.filetransfer.feature_3.7.100.v20130605-1748/asl-v20.txt
/usr/share/java/ecf/eclipse/features/org.eclipse.ecf.filetransfer.feature_3.7.100.v20130605-1748/epl-v10.html
/usr/share/java/ecf/eclipse/features/org.eclipse.ecf.filetransfer.feature_3.7.100.v20130605-1748/feature.properties
/usr/share/java/ecf/eclipse/features/org.eclipse.ecf.filetransfer.feature_3.7.100.v20130605-1748/feature.xml
/usr/share/java/ecf/eclipse/features/org.eclipse.ecf.filetransfer.feature_3.7.100.v20130605-1748/license.html
/usr/share/java/ecf/eclipse/features/org.eclipse.ecf.filetransfer.feature_3.7.100.v20130605-1748/notice.html
/usr/share/java/ecf/eclipse/features/org.eclipse.ecf.filetransfer.httpclient4.feature_3.6.1.v20130605-1748
/usr/share/java/ecf/eclipse/features/org.eclipse.ecf.filetransfer.httpclient4.feature_3.6.1.v20130605-1748/about.html
/usr/share/java/ecf/eclipse/features/org.eclipse.ecf.filetransfer.httpclient4.feature_3.6.1.v20130605-1748/asl-v20.txt
/usr/share/java/ecf/eclipse/features/org.eclipse.ecf.filetransfer.httpclient4.feature_3.6.1.v20130605-1748/epl-v10.html
/usr/share/java/ecf/eclipse/features/org.eclipse.ecf.filetransfer.httpclient4.feature_3.6.1.v20130605-1748/feature.properties
/usr/share/java/ecf/eclipse/features/org.eclipse.ecf.filetransfer.httpclient4.feature_3.6.1.v20130605-1748/feature.xml
/usr/share/java/ecf/eclipse/features/org.eclipse.ecf.filetransfer.httpclient4.feature_3.6.1.v20130605-1748/license.html
/usr/share/java/ecf/eclipse/features/org.eclipse.ecf.filetransfer.httpclient4.feature_3.6.1.v20130605-1748/notice.html
/usr/share/java/ecf/eclipse/plugins
/usr/share/java/ecf/eclipse/plugins/org.eclipse.ecf.filetransfer.jar
/usr/share/java/ecf/eclipse/plugins/org.eclipse.ecf.identity.jar
/usr/share/java/ecf/eclipse/plugins/org.eclipse.ecf.jar
/usr/share/java/ecf/eclipse/plugins/org.eclipse.ecf.provider.filetransfer.httpclient4.jar
/usr/share/java/ecf/eclipse/plugins/org.eclipse.ecf.provider.filetransfer.httpclient4.ssl.jar
/usr/share/java/ecf/eclipse/plugins/org.eclipse.ecf.provider.filetransfer.jar
/usr/share/java/ecf/eclipse/plugins/org.eclipse.ecf.provider.filetransfer.ssl.jar
/usr/share/java/ecf/eclipse/plugins/org.eclipse.ecf.ssl.jar

#------------------------------------------------------------------------
%prep

%build

%install
cd %{buildroot}
rpm2cpio %{SOURCE0} | cpio -id
