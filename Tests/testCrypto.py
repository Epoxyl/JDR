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

  m = b'gAAAAABeqdkEqKcjLRjxOfpfpQN6K2Nd4qXBT0VtKKcmJIoY5KP4BHqoDVSR_oy8mB8oQXWElWNsuNE5G5vvqfZdkVMXgoPbYm2wDyzVg9eZTV6k8b5stjuYIbvNqtFSWmPNE121sOMe9nMYPNFeBYYSPVX3l3jpp7e2_D_6mME0byUKAH7XU87KbXQL_y7gBR7fPMka5Tg-TzNVOiFHQeJs5_BeDx5h20-8upeNL1X2-TqZtCsIEklQkljWvg3AxSVjrWvUEauhsvg9V4uz04uronayWrZnCc-fF75NEYh22coasPVkOOmeyS-_2lQMtqzMivpjg8U4E34wB0mcq-l6kvsq4t7aaqLU33S3YWmxudvqCrivuL8Um1yWAXaMYYJ0Qx0JBsEWvSX7gTEeqNoe2aH_Kv62I3-Wqjq5lnp6kVfLuVzZCgtPYEbhTSQ01rlAv_5vhyjBBdCHkehjMd6d41Zk6FziL7vqxc6MsoveJzlMQvdFFhCTedz2vUSCe0lMeap1jRdgUj0Ub4ko0jtGW6vNYb6dO4HYE9l5iv8PIH5JELww0lPgo_4VvMvD6N12Rw94JRBvLvOUrVVsDRcK5Y8tn5u44GddIvU3edpX0mFn09LUEd9lpsqkfD8Ff4DTRMj8WRSF6zJpvR0JGQlnKtmSmsEMlWkq2CuDsHPXicjtyv4RfbuYiIUdYXQ-Oo-De6wkAKzECb0ywqOrc61sNrhlNLegBAOuemBSH3xEfpRPeludbJ1X1WwWTphiUnGliUgPRjBgqRz0-kHmvvjQFWbopbifoDllxNAtiaZlv5xtuGS55IlOAo_ahBGx97Ib7bihNuGGPSQoaFY2y1v7M_KeGGLSI9zGXMrjp84UQaR7p3tN-mEJZUJjcaxjyQRx6FIhox5gZncFYhXQvc9jW0ARnkXm6_3evkHcwlUV-A5l18zvWXvpm09Q0HDD9oGY6kYF67VgjN76xzYM-ThOIC3w--zxTCvDLue6ZEaCiFkRIpxL4Pmp3YwM9mfRbX5ds-H3ed1TPe_TIwJXL5Dyzc5zOLB7z3wQmmse7ZZVzQKUqqcg3DXS79MWHflV8cZUn4eom79ZRQO5YonxlQlNU-cs7goufDCx52Ytps-Vt9XYzHf9BP6Asb3eJGVyyhbCOUbBej8TElmFT_W2xAHQNnHNkn2URN-ilJz3Y_ZvFnLK03D7XWpn43--_wR6WQf7S7hsSThf66rHkqUXfJGYnC7kIQMgZ5y1sjGNG6RTW8EKgPgxY2-Jh2lV_zCzB3s_YIL6dSufPmkDpeccsGMoqsWJA5_onQnGQshExY2f-P4dxjW-UUwYjFHtqLRUsyDUwT7GTUIuuQ5nXS7xsw29sxj8RZLzAhXOBK7wsZIhx7-WHSfxEx5JWGQcXM7Vcx5_K7ySdMEKj3_g5WvhchSc7YhFgHqBP_654Cn5PhWJGAU-0xXdWnrzampLa8hCcVY3_Hgnc00tJ2btFBnLW_mGxBhtLu47jAQdnHLiwsfucqdwbPI9IX6OITv7u2DmH2kgAH3G2RI2OkC4a5yxrUWB7h0q6vYUiGCSWTaVM49AcGhnDvhGm-OWsMQxpP2KkCQhBNWStPxsCtosv4BpKFAFlPSS61OU_RnykdwGbgwIjrO7irvIWvs4wg5OgD9LLdsnQGNRuBLaU-U7By5iTvwS_oVZsUIsnw_NInbk99ilwwxGKxMdj7y_GdpdrBVYyHtft6caYPnWi_PMSl1HHyvcylOYPnKYoIIxnJb5GWuqtdff4QDMHEjJzCc0FvgmyRppxysNN4zlZtaFxQvahheHcY6pDxtp8_kh49FhSeNB4b8pyspAguw='
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
