Lessons Learnt 


• Committing within the pre-commit hook without the proper flags, such as [--no-verify], may lead to repository crashes by triggering an infinite loop.
• It is advisable to include 'git commit --no-verify' in the pre-commit hook to incorporate newly generated report files in the next git push.
• Setting up conditional blocks in the pre-commit hook allows checking committed changes against specific constraints. This helps prevent unnecessary reports, allowing developers to focus on relevant checks related to code changes in specific commits.
• Collaborators can share automated checks and scripts by including named directories containing these scripts within the repository.
• Collaborators can configure their git to use these shared scripts using a 'git config' command, for example, 'git config core.hooksPath .githooks'.

Additional report will be uploaded in a pdf file since it has images