from cryptography.fernet import Fernet
import time
import sys

def test():
  key = Fernet.generate_key()
  f = Fernet(key)
  msg = "Ceci est un test"
  token = f.encrypt(msg.encode())
  ret = f.decrypt(token)
  msg = "test"

def decryptWithKey(msg, key):
  f = Fernet(key.encode())
  return f.decrypt(msg.encode()).decode('utf-8')

def encryptWithKey(msg, key, enigma=False):
  f = Fernet(key.encode())
  encrypted = f.encrypt(msg.encode()).decode('utf-8')
  if enigma:
    return encrypted[-46:-1]
  return encrypted

def test2():
  serrure = ""                                    # ENIGMA KEY HERE


  f = None
  if serrure:
    k = serrure.encode()
    f = Fernet(k)

  m = b'gAAAAABeqev51HYpIrcu8xIhMMrqsBMko6Q4zV5WD2zXheXzxiCUZUcAiXRcgjbSEyxyNNa3YmcQoHy_r5NMUyd6kEmNFXD36rr9JWT5DSoVBpg8uHw2e7ql16SokcQugmNFrFukcnYdxu0XR9GkXoIrhaHvRhjwCFUwqMcDAfi-grFgTxJWn4GTHDuWydt16_uR_rxS7TlTS5I9xcZqJoeNBkQYcKcgMLXtYaJXotytq0a-kaYWAV-vp4_cVA6NOyfU-0r9OV2wSL_8-FNKta137cLoeKOqNqvnGAy57nu2-HccPmfUZyzLlECe8d8X1nrekpjKeFZ_tHnP2S1exyLCin0iBS1pSZmS7cmv-Z4AmJh0EpbhYXa36TAtwcVu5nA7U1cGWbqGyY2LrK11j_JLx5OIGz41-ImaeTZxutlzVBpeb33veyeKDqHxGoAwXiu-KZnXLtz2HKZ30mmc9jHMyBfRXiACZWvbN0ISbvdXwrOVpSFusWivFrGF2FhpyyjFF3rr-Dzs4xLSQyOlw-DjcEHhTRBgvqKAUZR4zbxbB9NFQ8a71IcRHPuDKqCI7_lEFKbzjmc_iG3vTSEs9A5EpAWC0VKxxtkfT-u8YsZZxA4Ik_J5CFwiHDx-20RsBnf0mFr2lrKJyNuc3rHjLJqUcpflFThjNCv4ngTG15bsqlFWOWQLBiMv0iRSUBlL5SwSJPWSq0jpV-4W4US_DAx3d1RYBQJILe6XmYe4huJomY3pgi43WKUfyKV46SyCp9ntjQiEYEpsLjCaBRp-nDYufJjQoCnYIgLkMP2pctxsX_TQcL0xi53ioly-iH95Z3FvxnPopz4Gda9ibJERBLmHYUi-Kj4IyjUXye3qWqSfa1q5VP9G3edxNml38X_-0FXShB5h9ryE-v5UjpStAzHjJlnK46cB5qRbzNvmSwLPG9Tc9bbTuf6FoHdpOjXF5-9KpShpiauIiA2fVHGBv_jsn9X9HObn9wInspCwLf_PqmFqzOkIb2URcyYRw1_nj6lJVFn_Qa-XqdfifLJiFNZhb_IGQODuEtlkgrsYy9bfNr7vA7E6khE5Fg-Osecvay6SMxqLTXw7T-o8q1YGvxy6or6I7jfDaDvt-tENj3EUL8y1zIzvzE3oybjE7vWixP439c1SJ9IqnsejsFCbSB4KdicZyi42-7CjB1ayobTxQ4PyKQYlDjMQeLjlyn6gm8k2l7pz1ZPZtuhx5Xb1BCr7sSEL5TXfFSKGhBfxSn5qAD7IpX-NukXIFHvYEmZmT8ZPgpNo6A5i16zu1kFeU7bUkgVD6CMQFnXOkajHp5ZXWPdzE1nU_UDM57uiYEbb08aTxduhYyRWcxQiZCFYEn96VtmrWWZ8VspEs7PrLzd0WVtHpLCQzN6sR0qnb30zhThH-mts1JVTemb_nc72AqQzT-Jk1zKmpRXprXjpzjnpq8m4HXqfL6hBufifvQKGL64bZ8YL-IWn1xykZiSh8nm2koA971zYf5KfMwCZhmGzAKyvF0nCQBCDqWrrgTQ1LpGymm0kolv5'

  if f:
    s = f.decrypt(m).decode('utf-8')
  else:
    s = m
  print(s)
  reponse = int(input())

  if reponse != 1:
    print("Nope !")
    return

  serrure = ""
  f = None
  if serrure:
    k = serrure.encode()
    f = Fernet(k)

  m = b'gAAAAABeqe6CLhu1Si5uJzDSW5lZbIEHY34W1beG20wdbBOeg__Lmjy3vhqOOnDBtO0ohM0t_A1d3K5e_UcRmh0sUcIQboXAw8htXjWBA_TEtiIB1a7V3ZOlJyLmkEk9vhHUbvv5kGLLKQlrGPqTlFN9gU7Af2nAQfS6DTq1tbhMh24oKRjbDRU8KeRRADg9CVMQHZRjKo5W6918axPf-rXii45eNURGCI488t70veb6FYwaFwQSjguMAlXaBCU3SDTKOUq9cYv7xYQ1KFHFyolFCwoe4Yw8yzS1wGZfPNtgoc1hxM51zO2mJfuvIQMYezLJ0c2fVLLe2W412vIHa1pHAfjDem5HznGynUu9MWKrYoYunxUhdD10529Smv-amUYcm6WmDuB3nOLqCiXvTuhobtgjUnXDo8D1CTcmYx63RZXWLD3ZI4pTvLdzOnIE2iA4WK4VMTuF_xSGZlUJWBrwtFBA9BYDW2YkuwFcIGAXkVZJiK8YW9dCv-C3yvtLNmhUEog-W9a6dq4qmd6S-f4Z4SO0JxOUp1HVWHkppBt-WsoEbmQS9mfPW-eZELfM5je4vvHP-dF0fZaxNVXwPq6PjsFFWRRANyzj-rmaE4STFNDOdD_bDPwD5DAySn4VtpJLZXWewXFaQwugjbJ6T8Y4kwmVBjPq0N9m96k3F73yTBQ0lPzOo8cKQ6PlABaWvP8TWJ2jkYdy'

  if f:
    s = f.decrypt(m).decode('utf-8')
  else:
    s = m
  print(s)

  reponse = int(input())
  if reponse != 2:
    print("Nope !")
    return

  print('\n')

  serrure = ""
  f = None
  if serrure:
    k = serrure.encode()
    f = Fernet(k)

  m = b'gAAAAABeqey5Axv3OtjvE6lrI-LY8w-KMYCfeCN-9Wp-KXf3AceZgM_I76g0tUUBuuByy7xE6ztIESUerhsxB0pxM4KNtBd172oGnuRo18UfeKH-CbqwUS7i_NzCpWxRnlrHeW91XC6_-3v08UV72cav7sC8HQBPgHy5oRkufslKq1VbZ1_BVSfWfGDxyyw0iOP3_qytrKm9yOjVOeiXLdfsStu8jUDJvatsTxYVpAaylg8auFtTjuF2JwV0IfsgXk2TW99bUqb6P9w5gfE7x3zrOMcL1HCVGSltbuiKW7J70p7iBz4q5LQKUD0sJ5Th9iL1XbH-0UYU8hGodFQr4Kq9iuRj3QlbSlA9n_H74JlN9vm1Vbc6ddQq0NwOy9sIXT9Fs3r4vmtIbGl8Kq4OHX4ywX3FreNlgQsi-BLoPYyPsq0_dR_38fnPGBFWMh_gb5rGNSrPJfzbEKb06551WsUnPfLgO5pgyrcHT1PowNP-Cy9C04FC8J3AiykU3FDy6fwDTZOHMfRKIRUbYFIcblmCl2mtRNG0hrQFgsqgTuji0Ly3YD7_g1guglTnmBGU6Mot_JOHvvmqkwV2kDT61r6D-RpSPJJCkNlu57LuQV_xHWyCObx28i64LMcWWAYGlxPNhUp82nHSn_FTKPQ11rXTCLE-EFvHBnHX9S94hXKrMyaRPq1kE385z96Mwj3QZl8wjACuLX2Z'

  if f:
    s = f.decrypt(m).decode('utf-8')
  else:
    s = m
  print(s)

  reponse = int(input())
  if reponse != 1 and reponse != 2 and reponse != 3 and reponse != 4 and reponse != 5:
    print("Nope !")
    return


  serrure = ""
  f = None
  if serrure:
    k = serrure.encode()
    f = Fernet(k)

  m = b'gAAAAABeqeTW4UVwCj9qOPWFeg1HsCIGG2DLt3jm5-7zUAtxigD4x8aVgJKOoL6_WLOIna5Rmi_3mv3g828XdBOD5JW9eoeLdqr7MPdRFdNuczmxQrBjz-zcqLG9XL4rWOsJG29shrta_hLKFWRU_92zMHi7I9kkTb7h9WN1KKgZWwdI1yeCdL0Gp1wc37mci2gGNV-qZjNxH5XbAQaMgeuBibXZSao6-zszePIhbruvTkp5RkicibNOm3Saz0piZRfm5xqgvX_l7j82rauXLJVgM3nZXWDSaoUyoZBGaZTqPkMBFNeqh0GhESMsEKlSgctTcm-7sroujiMsJX37ZkLvwWlPRkuynQ=='

  if f:
    s = f.decrypt(m).decode('utf-8')
  else:
    s = m
  print(s)

  reponse = int(input())
  if (reponse-1542358859/12) >= 42:
    print("Nope ?")
    time.sleep(5)
    for i in range(20):
      sys.stdout.flush()
      print(".")
      time.sleep(0.5)
  else:
    print("Nope !")
    return

  serrure = ""
  f = None
  if serrure:
    k = serrure.encode()
    f = Fernet(k)

  m = b'gAAAAABeucbROv8wQdZqxwRE_SoxRXvJYcKy5Gxze2aSXd5qLFXRfU7OeuksinujcHJASGlnemgGaZdBmHqBYkwW_KqTmrtVTRn-7rxI2M9o_3Ti8pzxEPHt-cHWCkULH7PGfTZ3uXxzSgcWQXk17qbIsqvcIAdBZitgFlEujd7NKlO9Zc1KbW71nxCBQrvLoV_1Xxrs5UwTyARcjJp6eMMCgRXTSIaxIUCmr4LrStjTal88bBtFAfiLe4Y074is4h_EBpFWz5VSe713z5pgpaAGmP7htLdUPI1D7A1LjWb2HW7csQMKVwzUEge7HVPDww0l8r34Cd8ihg3YZKUAJRORA9oD4wk8zajCJN0by0C5d5wTBCcL_qmO1wXgYa4EHqToQAt0LqeiepMj7cawrkEGVwIp_JOappg5MbJYJDp_edVqmbd6vlxtyjc2JC9dX8mfEqObwcb17Giquel-K2wM7hGVnLS8krhmUm8C4A7JckFImaUwQ6syGx_UTOsFieSh-2KpJZwfHkDXAbnCqkEGAxy3h6JH0Ani9p1FfWmmWeCnzSAl4yhe7NAjS7jFJte2dRFWIjVWsVLJVJjSR5axjqjliy2rz6aulGELCh3RcvvYO7yaQ763260cwCvgic6WeO84CZD2z6PBcSPKfVc4mVT9PaT05V_isfolHDr7aJRpBNK-IlIMe0XCgJZhNpVsk76-CaYA7_J0B9IzReSOMRHscwrSzrkYjFfe8oYoYw8c0mtzwzWpBJ5yB8cllnEI9tgcFdT9jk9JSBG8FPkUMIDJSH2gDlDBhLH9cQR82m1rKdQkTiF8DeBpB4AKE4sj3Hzu0m6zuHlhAPQ0HZDz9DkVPyouyZENgw6W4-Ud9FOXavlcXyQfgGtIeFWhOiQ8i4i8QMhO9UruihGg-RG-lXJBSkxiDiMPcSjQUV3vTGhWqKlscgRkSe_9_kTq4B-y7BIQBEihMiZWmhnOLKapJ00z2BYdlvdnkLBpamXUVhfg0rDMQ46fDUPQAMB4m68lbWd8XUWkj9Gdx4egwx1iu10ipijQ4bnaygEzYdTsvihexWaFFozi-sR8Vpcor9pX2henHU90Lq9kGG89KPNFzGs_tHSD7cdPriEiRG6YE_0E65vPTa-w3couPF5f2q2xi5NCF0MokRPYq7sa_DOInQVvXeH__eXBJxw6wjSMFrI0QVwdvOOaB-EDUYS0JiLWQmYAoWXywAbP3sWSND7OanUrzIqGLKBcI0abv5j0WQjQ2GnOVEKb3NvL96GXuiXha9hkA82S8S1ODDl9jttdB_Q7_q_AtLdbDdEEBiwr9PbZRKCaYQeu9JqgWffwdYHN1g-iKI-RyBVX71LNBfR_0Vx7N5mgCBZch8jCthqzafnuVdXrgIN7V22UEaB0CqJDleVGjavryRnV49P6vZQk0kvsDHj7383PuJCrz7KuGxGnpFdzccEI1SEObRZQjThquYcFHowpACgpfd2iGpR9UbcaldeXzbGDkp4vTtXw3-GX1Hdi7ISS7ZyVJLd10EG6SE_dDgYHZH_ZXlWLkQlHh0Pr7SjURi0iEddPlq72M7ROcUw44-r_RS7TgZcWbfHbGIq2ytPhTj9fOSkApPStIx4pOhNTBTJt8hatmx9qwxwl5hdgihhUzcNe5Wu1IOPX7Xl2X4nyaZ668jk1mfM3Dzio4zy_GSYhfpEAzWi7e_7UnXvbXJsOcc2zUfpGetUZr9v6nArIODTYxkrKl2G4GAdf-zRelBha2Z7-NIM552wKdE5l40pm6tajyrVhX5RzpoORie6SnwSTAtzU0DRjLxT1Eg3CCIClpBAQk_9I6jGtZpgvQRPjZEhgfae6fAZO_HAUHQHVXENzZD-Rw8mCfv3M16j8zPWp7fGbH6ga_AEyjzN5lW1kmBJrbt5Av2nCTre-dEGzT8cnYCErqA07rRtV8dzOHeeD8UgRXzwQ-JUFE0mAXLB9jmJV4gqK7FZeSbwp3cJCjLX0Y4pZ3_1X_8tcM-iEHtedRdoj7K47Hw3t3MHJO4QVGPvxoh7rPuFRed-5klT_yrSxJHAy3wsue9zlgPx3tajXa5kng441iloW7LTZ0B_s1xjvTPquiMVxNEM8mN02FRessnWsIUC2d-7CKWlqO3BU1ht8HmECmh96TNzHLJ8XIc-iQWOm8w17I-Czz9r8jb2MMZb8W09nAYS1FfqX5Hpwoq3Dj1IGk98ZxwXX_OQ='
  if f:
    s = f.decrypt(m).decode('utf-8')
  else:
    s = m
  raise Exception(s)

  print("Suite : ")

  serrure = ""
  f = None
  if serrure:
    k = serrure.encode()
    f = Fernet(k)
  print("\n")

  m = b'gAAAAABeqbNjGjfpS6OK7EWciOeTjtRVTBTfAYkQEUCqZ__TElhvZaUXoXI5sTt4o2b1s-kUE8NSsXxWIW8XAlizbnpSmZLPl3ScNvzcDt_8Dj8GDeMyG1K90CrYjfp945MXeeVeoBtEDApCSeXLp88SSbV_DEPRVnUjqDqFOaSlBnt0MV6hyqtogjhaOF_jb0aoViJTBHwvA7fdUFS84MQk4ufbQ974E9xVd5kOl--rhJDhW7CZiZ6QiAmfMwN5lzlb6Wjong3tUDCENRcy8sKdwcCJCyKNL37LWBpId_7pcoKUiXDGM09JH-Y6nApTCembcMcMpevCOJniptIfjorbOoiR7GL9XMNh3MMM08kdPyi5oNXrFw-GrUxkJrIwOpE2FWdZdu5irnrzGywUaz9tCPgxMPI8CFBrYPtmriGsEn77xdAnipAYRJupNlJHB7lDOW36YkUhQSM5ksJY26xRaaTEkqTPMXL7T1n9tYl4-bs5feRo7zf2Jq3kW3jP3DsQE996HRBVOno2E_DUM9RXDxUjsJbdLQ2EjLk3v84Ei9zhWaGvLor7tRRDtAK1R_SRAjBNOOfJw9MMxrZV6TgcVRNZIo1qssJU_Ur6_46kSlvB2NQXXdH0sitekxq3ZygbhLWRs6msNMbIXpQDqjfNZMz57Jm2EOPb5JF_S2PgEJW2SPkl9VDLJHyYxIGg2qYZgwXkKAarY6s6UvuJmBTl2MyV-BCIU_-BrUfsYSOv_CJff2L0d2Xzmbd36DCBq4pNYpwEwU4ABbii04KWRqHsxgv4I2-Cle3fK4rK3f_7kit-DgxV66HV0wGh_-PbTcDXj2VQnt3r1ah9vLHEJG7iA4KAV43tyIw0AQOqRBbvKSvI72bgjn3IARNnofAlJCSkEHWq1m8-FWCIahySBw4bWUfaKzO5fxGSeWMiPcAgVp-vFvIq2WSZkB5FJbmoEy3RqdymuY-EttmtCcuHM9KUfeQmxlwlw1DqZUC7R1jrfKoYVjJVX-uk2Pc7N9Bfb78FOcHzAeD8_NvDpTfoFt4xuCcf0-OOcVd4KxzsXvPYXMYh9AsVzldcFrHhAfB6NqZqGNS7Uol9pV3BkoVgYL3hl6ust9riPQ=='

  if f:
    s = f.decrypt(m).decode('utf-8')
  else:
    s = m
  print(s)
