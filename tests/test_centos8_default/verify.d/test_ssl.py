def test_verify_certificate(host):
    assert host.ansible(
      "command",
      "openssl verify -CAfile /etc/ssl/generated/ca/cert.pem /etc/ssl/generated/sub/cert.pem",
      become=True,
      become_user="root",
      check=False,
    )['rc'] == 0

def test_verify_certificate_without_ca(host):
    assert host.ansible(
      "command",
      "openssl verify /etc/ssl/generated/sub/cert.pem",
      become=True,
      become_user="root",
      check=False,
    )['rc'] == 2
