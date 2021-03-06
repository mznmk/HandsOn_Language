;--------------------------------------------------
; int slen(String message)
; String lenght calculation function
;--------------------------------------------------
slen:
	push	rbx
	mov		rbx, rax

nextchar:
	cmp		byte [rax], 0
	jz		finished
	inc		rax
	jmp		nextchar

finished:
	sub		rax, rbx
	pop		rbx
	ret

;--------------------------------------------------
; void sprint(String message)
; String printing function
;--------------------------------------------------
sprint:
	push	rdx
	push	rsi
	push	rdi
	push	rax

	call	slen

	mov		rdx, rax
	pop		rax
	mov		rsi, rax
	mov		rdi, 1
	mov		rax, 1
	syscall

	pop		rdi
	pop		rsi
	pop		rdx
	ret

;--------------------------------------------------
; void exit()
; Exit program and restore resources
;--------------------------------------------------
quit:
	mov		rax, 60
	mov		rdi, 0
	syscall
	ret
