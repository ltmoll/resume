"""Resume content returned by the API.

Keeping this information separate from the route makes it easy to update the
resume without changing how the server works.
"""

PROFILE = {
    "name": "Lucas Tremblay-Moll",
    "title": "Cloud Platform & Infrastructure Engineer",
    "location": "Montreal, Quebec, Canada",
    "email": "ltremblaymoll@gmail.com",
    "summary": (
        "Cloud platform and infrastructure engineer with 5+ years "
        "managing enterprise-scale workloads across Azure and AWS. "
        "Subject matter expert of cloud automation, Ansible, "
        "and operating system administration "
    ),
    "workstatus": "Canada/US Citizen, eligible to work in Canada and the United States without sponsorship.",
    "skills": [
        {
            "category": "Cloud Providers",
            "items": [
                "Microsoft Azure",
                "Amazon Web Services (AWS)",
                "Google Cloud Platform (GCP)"
            ],
        },

        {
            "category": "Programming & Scripting",
            "items": [
                "Python",
                "Bash",
                "PowerShell",
                "Java",
                "Ruby",
                "HTML/CSS/JavaScript(React)"
            ],
        },
        {
            "category": "CI/CD, IaC & DevOps Tools",
            "items": [
                "Ansible",
                "Chef",
                "Terraform",
                "Podman",
                "Docker",
                "Kubernetes",
                "Jenkins",
                "GitHub Actions"
            ],
        },
        {
            "category": "AI & Intelligent Automation",
            "items": [
                "AI-assisted coding (e.g., GitHub Copilot, OpenCode)",
                "LLM API integration",
                "Prompt design and output validation",
                "Agent orchestration and workflow automation"
            ],
        },
        {
            "category": "Operating Systems",
            "items": [
                "Red Hat Enterprise Linux",
                "Debian Linux (Ubuntu)",
                "Windows Servers",
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
                        "Architecture, administration, and optimization of the global Red Hat Ansible Automation Platform (AAP)",
                        "Ansible playbook development, troubleshooting and best practices",
                        "Day-2 VM automation catalog of 60+ Windows/Linux playbooks including hardening (CIS/NIST), agent management (Tanium, Qualys, NewRelic, Carbon Black) and OS configurations)",
                        "Managed and developed global cloud resource provisioning workflow integrating ServiceNow, Terraform, Azure/AWS and Ansible"
                    ],
                },
                {
                    "title": "Associate Infrastructure Reliability Engineer",
                    "dates": "March 2021 – March 2025",
                    "highlights": [
                        "Managed cloud compute, networking, storage, and recovery services across Azure and AWS, including virtual machines/EC2, VNets/VPCs, managed disks/EBS, and backup services.",
                        "Automated disaster recovery testing, backup validation, and failover workflows with PowerShell across Azure and AWS.",
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
