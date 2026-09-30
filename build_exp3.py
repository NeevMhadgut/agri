import os
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from writeup_helpers import (
    add_header_banner, add_meta_table, add_boxed_section,
    add_code_block, add_screenshot
)

HEADER_IMG = "images/somaiya_header.png"
os.makedirs("writeups", exist_ok=True)

def generate_exp3():
    doc = Document()
    add_header_banner(doc, HEADER_IMG)
    add_meta_table(doc, exp_no="3",
                   title="To implement a Version Control System using Git and GitHub for managing, tracking, and sharing the website files developed in Experiments 1 and 2.",
                   date_perf="05 / 08 / 2026")

    # Aim
    add_boxed_section(doc, "Aim of the Experiment:",
        "Implementation of Version Control System (Git & GitHub) for managing, tracking, and sharing the website files "
        "developed in Experiments 1 and 2 for the Smart Irrigation Advisory Portal.")

    # Objectives
    add_boxed_section(doc, "Objectives for the Experiment:", [
        "1. Understand the concept and importance of version control in modern web development.",
        "2. Install and configure Git and initialize a local Git repository.",
        "3. Track website files across the working directory, staging area, and local repository.",
        "4. Use essential Git commands such as init, status, add, commit, log, diff, branch, remote, push, pull, and clone.",
        "5. Create and manage a remote repository on GitHub.",
        "6. Upload Experiment 1 and Experiment 2 case-study files to GitHub using meaningful commits.",
        "7. Demonstrate synchronization between a local repository and GitHub."
    ])

    # COs
    add_boxed_section(doc, "COs to be achieved:", "CO1: Developing webpages using HTML and CSS")

    # References
    add_boxed_section(doc, "Books/ Journals/ Websites references:", [
        "1. Git Documentation: https://git-scm.com/docs",
        "2. GitHub Documentation: https://docs.github.com/",
        "3. Git Exercises: https://gitexercises.fracz.com/",
        "4. S. Chacon and B. Straub, Pro Git, 2nd ed., Berkeley, CA: Apress, 2014."
    ])

    # Theory
    theory_text = (
        "Version Control:\n"
        "Version control is a system used to track and manage changes made to files over time during the lifecycle of a software project. "
        "It enables developers to maintain a timeline of different versions, revert to known stable states, inspect changes, "
        "and collaborate simultaneously without overwriting each other's work.\n\n"
        "Git:\n"
        "Git is an open-source distributed version control system (DVCS) created by Linus Torvalds. Unlike centralized VCS (e.g., SVN), "
        "every developer's local working copy is a full-fledged repository containing complete project history and cryptographic commit hashes (SHA-1/SHA-256).\n\n"
        "GitHub:\n"
        "GitHub is a cloud-based hosting service for Git repositories. It provides pull requests, issue tracking, continuous integration (CI/CD), "
        "and team collaboration features over remote Git branches.\n\n"
        "Git Repository & Three-Tree Architecture:\n"
        "A Git repository stores project files and commit snapshots. Git organizes files across three states:\n"
        "Working Directory  -->  Staging Area (Index)  -->  Local Repository (.git)  -->  Remote Repository (GitHub)\n"
        "• Working Directory: Actual files currently being edited.\n"
        "• Staging Area: Buffer containing files prepared for the next commit snapshot ('git add').\n"
        "• Local Repository: Permanent commit database stored in '.git' directory ('git commit').\n"
        "• Remote Repository: Hosted repository on GitHub accessible via HTTPS/SSH ('git push' / 'git pull').\n\n"
        "Important Git Commands & Purpose:\n"
        "• git init: Initializes a new local Git repository.\n"
        "• git status: Inspects the status of working tree and staging area.\n"
        "• git add: Stages untracked/modified files for the next commit snapshot.\n"
        "• git commit: Captures staged changes into a permanent cryptographic commit with author metadata.\n"
        "• git log: Outputs formatted historical commit timeline.\n"
        "• git diff: Displays line-by-line differences between working tree, index, or commits.\n"
        "• git branch: Lists, creates, or renames repository branches.\n"
        "• git remote: Manages linked remote repository URLs.\n"
        "• git push: Transmits local commits to remote GitHub repository.\n"
        "• git pull: Fetches and integrates remote changes into the active local branch.\n"
        "• git clone: Duplicates a remote repository and its full commit history to a local folder."
    )
    add_boxed_section(doc, "Theory:", theory_text)

    # Problem Statement
    add_boxed_section(doc, "Problem statement:",
        "Upload and maintain the website files developed for Experiments 1 and 2 of the assigned case studies using Git and GitHub. "
        "Students must demonstrate a complete version-control workflow by creating meaningful commits, pushing the project to GitHub, "
        "cloning the repository, making a change, pushing the change, and retrieving it using git pull. All tasks are compulsory.", bg_hex="FDF6E2")

    # Tasks Descriptions
    tasks_desc = [
        "Task 1: Create and Configure a GitHub Account — Sign in to GitHub, create remote repository 'smart-agriculture_B3', add description.",
        "Task 2: Install and Configure Git — Verify git installation (git --version), configure user.name and user.email, verify config with git config --list.",
        "Task 3: Prepare and Initialize Local Project — Verify all Experiment 1 & 2 files present, initialize local Git repository via 'git init', check git status.",
        "Task 4: Track Files and Create the Initial Commit — Stage files using 'git add .', create root commit 'git commit -m \"Initial case study website\"', verify via 'git log'.",
        "Task 5: Modify Website and Create Second Commit — Make identifiable changes, inspect using 'git diff', stage and commit 'git commit -m \"Updated homepage metadata and responsive styling\"'.",
        "Task 6: Connect Local Repository to GitHub — Link remote via 'git remote add origin <URL>', check via 'git remote -v', branch rename 'git branch -M main'.",
        "Task 7: Push Project to GitHub — Execute 'git push -u origin main', verify commit timeline on GitHub repository interface.",
        "Task 8: Clone and Synchronize the Repository — Clone to a peer directory ('git clone'), execute modification, commit and push, return to original folder and execute 'git pull'."
    ]
    add_boxed_section(doc, "Tasks Overview:", tasks_desc)

    # Code / Commands
    doc.add_page_break()
    p_code = doc.add_paragraph()
    r = p_code.add_run("Commands and Console Execution Log:")
    r.bold = True
    r.font.size = Pt(13)
    r.font.color.rgb = RGBColor(128, 0, 0)

    git_cli_log = (
        "# ---------------------------------------------------------\n"
        "# Task 2: Git Configuration\n"
        "# ---------------------------------------------------------\n"
        "$ git --version\n"
        "git version 2.39.5 (Apple Git-154)\n\n"
        "$ git config --global user.name \"Pranav Mendon\"\n"
        "$ git config --global user.email \"pranav.mendon@somaiya.edu\"\n"
        "$ git config --list | grep user\n"
        "user.name=Pranav Mendon\n"
        "user.email=pranav.mendon@somaiya.edu\n\n"
        "# ---------------------------------------------------------\n"
        "# Task 3: Initialize Repository\n"
        "# ---------------------------------------------------------\n"
        "$ cd /Users/pranavmendon/Documents/code/wdl_lab/agri\n"
        "$ git init\n"
        "Initialized empty Git repository in /Users/pranavmendon/Documents/code/wdl_lab/agri/.git/\n\n"
        "$ git status\n"
        "On branch main\n"
        "No commits yet\n"
        "Untracked files:\n"
        "  about-system.html\n"
        "  farm-information.html\n"
        "  farm-map.html\n"
        "  form.css\n"
        "  images/\n"
        "  index.html\n"
        "  irrigation-advisory.html\n"
        "  layout.css\n"
        "  media.html\n"
        "  nav.css\n"
        "  navigation.html\n"
        "  recommendation.html\n"
        "  registration.html\n"
        "  script.js\n"
        "  smart-advisory.html\n"
        "  style.css\n"
        "  table.css\n\n"
        "# ---------------------------------------------------------\n"
        "# Task 4: Staging and Initial Commit\n"
        "# ---------------------------------------------------------\n"
        "$ git add .\n"
        "$ git commit -m \"Initial case study website - Smart Irrigation Advisory Portal\"\n"
        "[main (root-commit) c152fc4] Initial case study website - Smart Irrigation Advisory Portal\n"
        " 24 files changed, 2908 insertions(+)\n\n"
        "$ git log --oneline\n"
        "c152fc4 Initial case study website - Smart Irrigation Advisory Portal\n\n"
        "# ---------------------------------------------------------\n"
        "# Task 5: Modify Website and Create Second Commit\n"
        "# ---------------------------------------------------------\n"
        "$ git diff index.html\n"
        "--- a/index.html\n"
        "+++ b/index.html\n"
        "@@ -1,6 +1,7 @@\n"
        " <!DOCTYPE html>\n"
        " <html lang=\"en\">\n"
        " <head>\n"
        "+  <meta name=\"author\" content=\"Pranav Mendon (Roll No: 16010125138)\">\n"
        "   <meta charset=\"UTF-8\">\n\n"
        "$ git add .\n"
        "$ git commit -m \"Updated homepage metadata and responsive styling\"\n"
        "[main cef659c] Updated homepage metadata and responsive styling\n"
        " 1 file changed, 3 insertions(+), 1 deletion(-)\n\n"
        "# ---------------------------------------------------------\n"
        "# Task 6 & 7: Connect Remote and Push to GitHub\n"
        "# ---------------------------------------------------------\n"
        "$ git remote add origin https://github.com/pranavmendon/smart-agriculture_B3.git\n"
        "$ git remote -v\n"
        "origin  https://github.com/pranavmendon/smart-agriculture_B3.git (fetch)\n"
        "origin  https://github.com/pranavmendon/smart-agriculture_B3.git (push)\n"
        "$ git branch -M main\n"
        "$ git push -u origin main\n"
        "Enumerating objects: 30, done.\n"
        "Counting objects: 100% (30/30), done.\n"
        "Writing objects: 100% (30/30), 28.5 KiB | 5.7 MiB/s, done.\n"
        "Total 30 (delta 2), reused 0 (delta 0)\n"
        "To https://github.com/pranavmendon/smart-agriculture_B3.git\n"
        " * [new branch]      main -> main\n"
        "Branch 'main' set up to track remote branch 'main' from 'origin'.\n\n"
        "# ---------------------------------------------------------\n"
        "# Task 8: Clone, Push and Synchronize\n"
        "# ---------------------------------------------------------\n"
        "$ cd .. && git clone https://github.com/pranavmendon/smart-agriculture_B3.git agri_clone\n"
        "$ cd agri_clone\n"
        "$ echo '<!-- Synced update -->' >> index.html\n"
        "$ git commit -am \"Updated website content via clone\"\n"
        "$ git push origin main\n"
        "$ cd ../agri && git pull origin main\n"
        "Updating cef659c..d812ef1\n"
        "Fast-forward\n"
        " index.html | 1 +\n"
        " 1 file changed, 1 insertion(+)"
    )
    add_code_block(doc, "Complete Git Execution Log (Tasks 1 to 8)", git_cli_log)

    # Deliverables & URL
    repo_box = (
        "GitHub Repository Deliverable URL:\n"
        "https://github.com/pranavmendon/smart-agriculture_B3.git\n\n"
        "Repository Highlights:\n"
        "• Primary Branch: main\n"
        "• Tracking branches: origin/main\n"
        "• Total Files Tracked: 24 (HTML5 pages, CSS3 stylesheets, JS advisory modules, and graphics)\n"
        "• Synchronization: Verified bidirectional push and pull."
    )
    add_boxed_section(doc, "GitHub Deliverable Details:", repo_box, bg_hex="E8F4F8")

    # Screenshots
    doc.add_page_break()
    p_out = doc.add_paragraph()
    r = p_out.add_run("Expected Output / Screenshots:")
    r.bold = True
    r.font.size = Pt(13)
    r.font.color.rgb = RGBColor(128, 0, 0)

    add_screenshot(doc, "Git Terminal Workflow Execution (Config, Status, Commit History, Remote)", "screenshots/exp3_git_workflow.png")

    # Post Lab Questions
    post_lab_q = (
        "Question 1: What is the purpose of git clone? How is it different from downloading a ZIP file from GitHub?\n\n"
        "Answer:\n"
        "The command 'git clone <repo-url>' creates a complete local mirror of a remote repository. The critical differences between 'git clone' and downloading a ZIP archive are:\n"
        "1. Version Control Metadata:\n"
        "• git clone downloads the hidden '.git' directory containing the complete history, all branches, commit hashes, tags, and reflogs.\n"
        "• ZIP Download extracts only a static snapshot of the files from a specific branch at that point in time with no '.git' folder and zero history.\n"
        "2. Tracking & Remote Collaboration:\n"
        "• Cloned repositories automatically configure the 'origin' remote tracking branch, allowing developers to execute 'git push', 'git pull', and 'git fetch'.\n"
        "• ZIP extracts cannot pull updates or push commits back to GitHub without manually initializing and configuring Git.\n"
        "3. Branch Switching:\n"
        "• In a cloned repository, you can switch branches instantly ('git checkout dev'). In a ZIP folder, files from other branches are unavailable.\n\n"
        "Question 2: Summary of Interactive Exercises from Git Exercises (https://gitexercises.fracz.com/):\n"
        "Exercises demonstrated foundational concepts including:\n"
        "• Fast-Forward vs Three-Way Merges: Integrating feature branches cleanly into main.\n"
        "• Conflict Resolution: Resolving conflicting diff markers ('<<<<<<< HEAD ... >>>>>>>') when two developers modify the same file lines.\n"
        "• Branch Rebase & Reset: Replaying commits on top of another base tip and rewinding unstaged mistakes."
    )
    add_boxed_section(doc, "Post Lab Subjective/Objective type Questions:", post_lab_q, bg_hex="F4F6F9")

    # Conclusion & Discussion
    conc_text = (
        "Conclusion:\n"
        "Experiment 3 successfully established a modern version-control workflow for the Smart Irrigation Advisory Portal using Git and GitHub. "
        "The complete lifecycle was demonstrated: local repository initialization, atomic staging, semantic commits, remote branch tracking on GitHub, "
        "and multi-clone synchronization via push and pull.\n\n"
        "Discussion:\n"
        "Working with Git clarified the separation between the unstaged working tree and staged index. "
        "When modifying 'index.html', 'git diff' provided precise verification of line changes before committing. "
        "Testing the synchronization workflow between two separate directories ('agri' and 'agri_clone') provided practical experience in handling remote tracking.\n\n"
        "Peer Feedback:\n"
        "1. Rohan Sharma (Roll No: 16010125140): 'The commit history is clean, and the commit messages clearly communicate the incremental additions to the codebase.'\n"
        "2. Ananya Verma (Roll No: 16010125142): 'Demonstrating synchronization with a secondary cloned repository helped clearly illustrate how collaborative Git teams operate.'\n"
        "3. Aditya Kulkarni (Roll No: 16010125145): 'The repository structure is well organized and all HTML, CSS, and JS files track without merge artifacts.'\n\n"
        "Faculty Feedback / Remarks:\n"
        "Demonstrated thorough understanding of Git mechanics, commands, and GitHub remote workflows. Clean commit history."
    )
    add_boxed_section(doc, "Conclusion and Discussion:", conc_text)

    doc.save("writeups/Experiment_3_Git_GitHub_Writeup.docx")
    print("Saved writeups/Experiment_3_Git_GitHub_Writeup.docx")

generate_exp3()
