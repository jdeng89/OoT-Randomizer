red_ice_alpha:
    ; set initial red ice opacity
    ; a0 = red ice actor
    lhu     t0, 0x001C(a0)  ; actor params
    andi    t0, t0, 0x1000  ; custom param flag
    beqzl   t0, @@return
    li      t7, 0xFF        ; opaque if unset
    li      t7, 0x8F        ; semitransparent if set
@@return:
    jr      ra
    sh      t7, 0x01F0(a0)
