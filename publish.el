(defun jethro/publish (file)
  (with-current-buffer (find-file-noselect file)
    (projectile-mode -1)
    (dtrt-indent-mode -1)
    (setq org-hugo-base-dir "~/braindump")
    (org-hugo-export-wim-to-md)))
