;; Package Installer Details
(require 'package)
(add-to-list 'package-archives '("melpa-stable"
				 . "http://stable.melpa.org/packages/"))
(package-initialize)

;; (defvar package-list)
;; (setq package-list '(async auctex auto-complete autopair clang-format cmake-ide
;;                            cmake-mode company company-irony
;;                            company-irony-c-headers dash epl flycheck
;;                            flycheck-irony flycheck-pyflakes 
;;                            google-c-style helm helm-core helm-ctest
;;                            helm-flycheck helm-flyspell helm-ls-git helm-ls-hg
;;                            hungry-delete irony
;;                            let-alist levenshtein magit markdown-mode pkg-info
;;                            popup rtags seq solarized-theme vlf web-mode
;;                            window-numbering writegood-mode yasnippet))
;; ;; fetch the list of packages available
;; (unless package-archive-contents
;;   (package-refresh-contents))
;; ;; install the missing packages
;; (dolist (package package-list)
;;   (unless (package-installed-p package)
;;     (package-install package)))

;; User Details
;; user-full-name is full name of the user logged in. Here overridden by setq special form.
;; Original value was gaurav.
(setq user-full-name "Gaurav Sood")
(setq user-mail-address "imgauravsood@gmail.com")
;; Global Settings
(prefer-coding-system 'utf-8)
(set-language-environment 'utf-8)
(setq locale-coding-system 'utf-8)
(set-default-coding-systems 'utf-8)
(set-terminal-coding-system 'utf-8)
(setq buffer-file-coding-system 'utf-8)
(column-number-mode)
(global-auto-revert-mode)
(global-linum-mode)
(global-company-mode)
(projectile-global-mode)
(helm-projectile-on)
(setq
 backup-by-copying t      ; don't clobber symlinks
 backup-directory-alist
 '(("." . "~/.backemacs"))    ; don't litter my fs tree
 delete-old-versions t
 kept-new-versions 6
 kept-old-versions 2
 version-control t)
(setq-default fill-column 80)
(add-hook 'prog-mode-hook `turn-on-auto-fill)
(add-hook `text-mode-hook `turn-on-auto-fill)
(global-flycheck-mode)
(electric-pair-mode)
(company-quickhelp-mode)
(add-hook 'prog-mode-hook #'rainbow-delimiters-mode)
(highlight-parentheses-mode)
(paren-activate)
(if (display-graphic-p)
    ;; (load-theme 'atom-one-dark t))
    (load-theme 'sanityinc-solarized-light t))
(global-set-key (kbd "C-c C-u") 'uncomment-region)
(global-set-key (kbd "C-c C-m") 'comment-region)
(tool-bar-mode 0)
(defalias 'yes-or-no-p 'y-or-n-p)

;; Mode Line Customization
(sml/setup t)
;; Haskell
(add-hook 'haskell-mode-hook 'intero-mode)

;; Python
(require `company)
(defun my/python-mode-hook ()
  (add-to-list 'company-backends 'company-jedi))
(add-hook 'python-mode-hook 'my/python-mode-hook)
(pyvenv-mode)
;;(pyvenv-activate)
(add-hook 'python-mode-hook 'py-autopep8-enable-on-save)
(add-hook 'python-mode-hook
	  '(lambda ()
	     (local-set-key (kbd "C-c .") 'jedi:goto-definition)
	     (local-set-key (kbd "C-c ,") 'jedi:goto-definition-pop-marker)
	     (local-set-key (kbd "C-c d") 'jedi:show-doc)
	     (local-set-key (kbd "C-<tab>") 'jedi:complete)))

;;Git
(require `magit)

;;Org Mode
(global-set-key "\C-cl" 'org-store-link)
(global-set-key "\C-ca" 'org-agenda)
(global-set-key "\C-cc" 'org-capture)
(global-set-key "\C-cb" 'org-iswitchb)
(org-babel-do-load-languages
 'org-babel-load-languages
 '((ditaa . t) (perl . t) (emacs-lisp . t) (python . t) (haskell . t) (C . t) (js . t)))
(add-hook 'org-mode-hook
          (lambda()
            (flyspell-mode 1)))
(defun my-org-mode-hook ()
  (add-hook 'completion-at-point-functions 'pcomplete-completions-at-point nil t))
(add-hook 'org-mode-hook #'my-org-mode-hook)
(org-update-checkbox-count t)

(when window-system
  (require 'org-bullets)
  (add-hook 'org-mode-hook (lambda () (org-bullets-mode 1))))

(require `org)
(setq org-agenda-files (append (file-expand-wildcards
				"~/Dropbox/orgagenda/*.org")))
(setq org-log-done (quote time))
(setq org-log-into-drawer t)
(setq org-log-reschedule (quote note))
(setq org-refile-allow-creating-parent-nodes (quote confirm))
(add-to-list 'org-refile-targets '((org-agenda-files :maxlevel . 1) (nil :maxlevel . 1)))
(setq org-refile-use-outline-path 'file)
(global-set-key (kbd "<f6>") 'org-capture)

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;;;;;;;;;;;;;;;;;;;;C++;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
(setenv "GTAGSLIBPATH" "/home/gaurav/.gtags/")
(eval-after-load 'company
  '(add-to-list
    'company-backends '(company-irony-c-headers company-irony)))

(add-hook 'c-mode-common-hook
          (lambda ()
            (if (derived-mode-p 'c-mode 'c++-mode)
                (cppcm-reload-all))))

(add-hook 'c-mode-common-hook
          (lambda ()
            (when (derived-mode-p 'c-mode 'c++-mode 'java-mode)
              (ggtags-mode 1))))

;; ;; OPTIONAL, somebody reported that they can use this package with Fortran
;; (add-hook 'c90-mode-hook (lambda () (cppcm-reload-all)))
;; ;; OPTIONAL, avoid typing full path when starting gdb
;; (global-set-key (kbd "C-c C-g")
;;  '(lambda ()(interactive) (gud-gdb (concat "gdb --fullname "
;; 					   (cppcm-get-exe-path-current-buffer)))))
;; ;; OPTIONAL, some users need specify extra flags forwarded to compiler
;; (setq cppcm-extra-preprocss-flags-from-user '("-I/usr/src/linux/include" "-DNDEBUG"))


;; (add-hook 'c++-mode-hook 'irony-mode)
;; (add-hook 'c-mode-hook 'irony-mode)
;; (add-hook 'objc-mode-hook 'irony-mode)
;; (defun my-irony-mode-hook ()
;;   (define-key irony-mode-map [remap completion-at-point]
;;     'irony-completion-at-point-async)
;;   (define-key irony-mode-map [remap complete-symbol]
;;     'irony-completion-at-point-async))
;; (add-hook 'irony-mode-hook 'my-irony-mode-hook)
;; (add-hook 'irony-mode-hook 'irony-cdb-autosetup-compile-options)

(custom-set-variables
 ;; custom-set-variables was added by Custom.
 ;; If you edit it by hand, you could mess it up, so be careful.
 ;; Your init file should contain only one such instance.
 ;; If there is more than one, they won't work right.
 '(custom-safe-themes
   (quote
    ("a27c00821ccfd5a78b01e4f35dc056706dd9ede09a8b90c6955ae6a390eb1c1e" "a8245b7cc985a0610d71f9852e9f2767ad1b852c2bdea6f4aadc12cce9c4d6d0" "3c83b3676d796422704082049fc38b6966bcad960f896669dfc21a7a37a748fa" default))))
(custom-set-faces
 ;; custom-set-faces was added by Custom.
 ;; If you edit it by hand, you could mess it up, so be careful.
 ;; Your init file should contain only one such instance.
 ;; If there is more than one, they won't work right.
 )
(yas-global-mode)

(put 'narrow-to-region 'disabled nil)
