;; Proxy Environment
(when (getenv "http_proxy")
  (setq url-proxy-services
	'(("no_proxy" . "^\\(localhost\\|10.*\\)")
	  ("http" . "web-proxy.atl.hp.com:8080")
	  ("https" . "web-proxy.atl.hp.com:8080"))))

;; Adding repos to package-archives
(require 'package)
(add-to-list 'package-archives '("melpa-stable" .
				 "http://stable.melpa.org/packages/"))
(package-initialize)

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;; Global ;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
(prefer-coding-system 'utf-8)
(set-language-environment 'utf-8)
(setq locale-coding-system 'utf-8)
(set-default-coding-systems 'utf-8)
(set-terminal-coding-system 'utf-8)
(prefer-coding-system 'utf-8)
(global-flycheck-mode)
(column-number-mode)
(global-auto-revert-mode)
(require 'company)
(add-hook 'after-init-hook 'global-company-mode)
(yas-global-mode)
(global-set-key (kbd "C-c C-m") 'uncomment-region)
;; Backup directory
(setq
   backup-by-copying t      ; don't clobber symlinks
   backup-directory-alist
    '(("." . "~/.saves"))    ; don't litter my fs tree
   delete-old-versions t
   kept-new-versions 6
   kept-old-versions 2
   version-control t)       ; use versioned backups
(setq dired-omit-files "^\\.?#\\|^\\.$\\|^\\.\\.$\\|^\\..*$")
(setq vc-msg-force-vcs "p4")
(require 'whitespace)
(setq whitespace-style '(face empty tabs lines-tail trailing))
(global-whitespace-mode t)

(setq fill-column 80)
(setq text-mode-hook 'turn-on-auto-fill)
(setq default-major-mode 'text-mode)

(require 'virtualenvwrapper)
(venv-initialize-eshell)
(venv-initialize-interactive-shells)
(setq venv-location "/home/gaurav/.virtualenvs")
(setq-default mode-line-format (cons '(:exec venv-current-name)
				     mode-line-format))
(require 'company-jedi)
(defun my/python-mode-hook ()
  (add-to-list 'company-backends 'company-jedi))
(add-hook 'python-mode-hook 'my/python-mode-hook)
(add-hook 'python-mode-hook 'py-autopep8-enable-on-save)
(setq jedi:environment-root "py3")
(setq jedi:environment-virtualenv (list "virtualenv" "--system-site-packages"
				       "--python"
				       "/home/gaurav/.virtualenvs/py3.5.2/bin/python3"))
(jedi:install-server)
(venv-workon "py3.5.2")
;;(setq jedi:server-args (list "--virtual-env" "
(add-hook 'python-mode-hook
	  '(lambda ()
	     (local-set-key (kbd "C-c .") 'jedi:goto-definition)
	     (local-set-key (kbd "C-c ,") 'jedi:goto-definition-pop-marker)
	     (local-set-key (kbd "C-c d") 'jedi:show-doc)
	     (local-set-key (kbd "C-<tab>") 'jedi:complete)))
(add-hook 'python-mode-hook 'jedi:setup)

;; (pyvenv-mode)

;; Haskell
(add-hook 'haskell-mode-hook 'intero-mode)

;; Org Mode
(global-set-key "\C-cl" 'org-store-link)
(global-set-key "\C-ca" 'org-agenda)
(global-set-key "\C-cc" 'org-capture)
(global-set-key "\C-cb" 'org-iswitchb)
(if window-system
    (progn (require 'org-bullets)
	   (add-hook 'org-mode-hook (lambda () (org-bullets-mode 1)))))

;; C/C++
(add-hook 'c-mode-common-hook
          (lambda ()
            (if (derived-mode-p 'c-mode 'c++-mode)
                (cppcm-reload-all)
              )))
(eval-after-load 'company
  '(add-to-list
    'company-backends '(company-irony-c-headers company-irony)))
(eval-after-load 'flycheck
  '(add-hook 'flycheck-mode-hook #'flycheck-irony-setup))
(add-hook 'c-mode-common-hook
          (lambda ()
            (when (derived-mode-p 'c-mode 'c++-mode 'java-mode)
              (ggtags-mode 1))))

;; Helm Projectile
(projectile-global-mode)
(setq projectile-completion-system 'helm)
(helm-projectile-on)
(put 'set-goal-column 'disabled nil)
(put 'narrow-to-region 'disabled nil)
(custom-set-variables
 ;; custom-set-variables was added by Custom.
 ;; If you edit it by hand, you could mess it up, so be careful.
 ;; Your init file should contain only one such instance.
 ;; If there is more than one, they won't work right.
 '(custom-enabled-themes (quote (sanityinc-solarized-light)))
 '(custom-safe-themes
   (quote
    ("0fa684b6cf782ee4fef96863b4921641c8b38c9d246f4bddd1e9277369c3e02a" "4cf3221feff536e2b3385209e9b9dc4c2e0818a69a1cdb4b522756bcdf4e00a4" default))))
(custom-set-faces
 ;; custom-set-faces was added by Custom.
 ;; If you edit it by hand, you could mess it up, so be careful.
 ;; Your init file should contain only one such instance.
 ;; If there is more than one, they won't work right.
 )
;; Latex

(add-hook 'LaTeX-mode-hook #'latex-extra-mode)

(global-set-key (kbd "M-p") 'ace-window)
