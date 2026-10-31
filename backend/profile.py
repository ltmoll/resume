"""Resume content returned by the API.

Keeping this information separate from the route makes it easy to update the
resume without changing how the server works.
"""

PROFILE = {
    "name": "Lucas Tremblay-Moll",
    "title": "Cloud Platform & Infrastructure Reliability Engineer",
    "location": "Terrebonne, Quebec, Canada",
    "email": "ltremblaymoll@gmail.com",
    "summary": (
        "Cloud platform and infrastructure reliability engineer with 5+ years "
        "of experience building and operating enterprise-scale systems across "
        "AWS and Azure. Focused on infrastructure as code, automation, "
        "reliability, and secure cloud operations."
    ),
    "skills": [
        {
            "category": "Cloud Providers",
            "items": [
                "Amazon Web Services (AWS)",
                "Microsoft Azure",
                "Google Cloud Platform (GCP)"
            ],
        },

        {
            "category": "Programming & Scripting",
            "items": [
                "Python",
                "Bash",
                "PowerShell",
                "Java"
            ],
        },
        {
            "category": "Automation, IaC & Platforms",
            "items": [
                "Ansible",
                "Chef",
                "Terraform",
                "Kubernetes",
                "Jenkins"
            ],
        },
        {
            "category": "Automation, IaC & Platforms",
            "items": [
                "Ansible",
                "Chef",
                "Terraform",
                "Kubernetes",
                "Jenkins"
            ],
        },
        {
            "category": "Operating systems",
            "items": [
                "Red Hat Enterprise Linux",
                "Ubuntu Linux",
                "Windows Server",
                "Oracle Linux",
            ],
        }
    ],
    "experience": [
        {
            "company": "Manulife Financial",
            "location": "Montreal, Quebec, Canada",
            "roles": [
                {
                    "title": "Cloud Platform Engineer",
                    "dates": "March 2025 – October 2026",
                    "highlights": [
                        "Led administration and reliability for the global Red Hat Ansible Automation Platform across AWS and Azure.",
                        "Built Terraform and Ansible workflows to deploy and manage more than 7,000 Linux and Windows virtual machines.",
                        "Automated operational tasks and patching with Python, Bash, and PowerShell in CI/CD pipelines.",
                        "Improved security and compliance with automated vulnerability management, endpoint protection, and zero-trust authentication baselines.",
                    ],
                },
                {
                    "title": "Associate Infrastructure Reliability Engineer",
                    "dates": "March 2021 – March 2025",
                    "highlights": [
                        "Managed Azure and AWS services, including virtual machines, networks, disks, resource groups, and recovery vaults.",
                        "Automated Azure Site Recovery failover testing, backup validation, and disaster recovery workflows with PowerShell.",
                        "Provided Tier 3 system administration and operating-system troubleshooting for enterprise infrastructure.",
                    ],
                },
            ],
        },
        {
            "company": "Group Dynamite",
            "location": "Montreal, Quebec, Canada",
            "roles": [
                {
                    "title": "Technical Services Representative",
                    "dates": "February 2015 – August 2021",
                    "highlights": [
                        "Provided Tier 1 and Tier 2 support for point-of-sale systems, store hardware, and network connectivity across retail locations.",
                        "Coordinated troubleshooting with external vendors to meet service-level objectives.",
                    ],
                }
            ],
        },
    ],
    "education": [
        {
            "school": "Dawson College",
            "credential": "Diploma of College Studies (DEC), General Social Sciences",
            "dates": "2015",
        },
        {
            "school": "Computer Science Technology coursework",
            "credential": "Shell scripting, Linux system administration, Java, and web development",
            "dates": "2016 – 2017",
        },
    ],
    "languages": ["English — native", "French — native", "Spanish — native"],
}
