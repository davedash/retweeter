import pytest

from retweeter.helpers import probably_english

NOT_ENG='目前CalFire尚未在#SanJose市內發布任何警告或疏散命令。 通過訪問來為迅速變化的條件做好準備 https://t.co/6e6DffhHlU. #SCULightningComplex'
NOT_ENG2='目前CalFire尚未在#SanJose市内发布任何警告或疏散命令。 通过访问来为迅速变化的条件做好准备https://t.co/6e6DffhHlU. #SCULightningComplex'
ENG='As of 8/21/20 at 11:00 a.m., CalFire has issued no warning or evacuation order within the City of San Jose. Be prep… https://t.co/5NWroKwRjV'

@pytest.mark.parametrize('text,expected', [(NOT_ENG, False), (NOT_ENG2, False), (ENG, True)])
def test_probably_english(text, expected):
  assert(probably_english(text)) == expected
