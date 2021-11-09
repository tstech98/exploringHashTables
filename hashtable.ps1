$hash = @{ ID = 1; Shape = "Square"; Color = "Blue"; Sides = 4; Dimension = "2D"}
write-host("____________")
write-host("hash keys:")
$hash.Keys
write-host("____________")
write-host("hash values:")
$hash.Values
write-host("____________")
write-host("get id:")
$hash["ID"]
write-host("____________")
write-host("size:")
$hash.Count
write-host("____________")
write-host("added a key value Home = Flatland")
$hash.Add("Home", "Flatland")
write-host("____________")
write-host("new size:")
$hash.Count
write-host("____________")
write-host("sort by the key:")
$hash.GetEnumerator() | Sort-Object -Property key
write-host("____________")