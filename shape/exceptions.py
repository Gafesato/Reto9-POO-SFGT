class ValorInvalidoArgs(Exception):
  """
  Excepción personalizada para cuando la longitud de args* no es válido.

  Args:
    message: Mensaje informativo sobre la excepción.
  """

  def __init__(self, message):
    super().__init__(message)