describe 'gksu', :type => :class do
  let (:facts) { { 'is_virtual' => 'false'} }
  # test verify with_ensure must be set to latest
  it { should contain_package('gksu').with_ensure('latest') }
end
