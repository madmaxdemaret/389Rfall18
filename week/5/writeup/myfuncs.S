section .text         ;declare this section to include executable instructions

global my_memset      ;export the 'my_memset' symbol to be accessible outside of file
my_memset:
        push rbp      ;saves the base pointer for the previous function's stack frame
        mov rbp, rsp  ;moves up the base pointer to the top of the stack to create a new frame

        ;so rdi = str*, rsi = val, rdx = len
	mov rcx, 0

set_start:
	cmp rcx, rdx
	jge set_exit
	
	mov [rdi+rcx*1], sil
	inc rcx
	jmp set_start
set_exit:
        leave         ;moves down the stack pointer to the current base pointer,
                      ;and restores our saved base pointer, effectively
                      ;restoring our previous stack frame
        ret           ;jumps to the top value on the stack, hopefully the return address!


global my_strncpy     ;export the 'my_strncpy' symbol to be accessible outside of file
my_strncpy:
        push rbp      ;saves the base pointer for the previous function's stack frame
        mov rbp, rsp  ;moves up the base pointer to the top of the stack to create a new frame


        ;;;;;;;;;;;;;;;;;;;;;
        ;your code goes here!
        ;;;;;;;;;;;;;;;;;;;;;

	;rdi = dst*, rsi = src*, rdx = len
	mov rcx, 0

cpy_start:
	cmp rcx, rdx
	jge cpy_exit

	mov r8b, [rsi+rcx*1]
	mov [rdi+rcx*1], r8b

	inc rcx
	jmp cpy_start
cpy_exit:
        leave         ;moves down the stack pointer to the current base pointer,
                      ;and restores our saved base pointer, effectively
                      ;restoring our previous stack frame
        ret           ;jumps to the top value on the stack, hopefully the return address!
