(defun jethro/publish (file)
  (with-current-buffer (find-file-noselect file)
    (projectile-mode -1)
    (dtrt-indent-mode -1)
    (setq org-hugo-base-dir "~/braindump")
    (if (>
          (string-to-number
            (shell-command-to-string
              (concat "wc -l < " (expand-file-name (file-name-nondirectory file)) " | bc")))
          300)
        (setq org-hugo-export-with-section-numbers 2))
    (org-hugo-export-wim-to-md)))
