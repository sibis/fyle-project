HOST="https://fyle-bank-data.herokuapp.com"
OFFSET_LIMIT=0
ENDPOINT="api/branches"
AUTOCOMPLETE_Q="Bangalore"
BRANCHSEARCH_Q="RTGS"
AUTOCOMPLETE_LIMIT=4
BRANCHSEARCH_LIMIT=10

BRANCHSEARCH_URL="$HOST/$ENDPOINT?q=$AUTOCOMPLETE_Q&limit=$AUTOCOMPLETE_LIMIT&offset=$OFFSET_LIMIT"
AUTOCOMPLETE_URL="$HOST/$ENDPOINT/autocomplete?q=$BRANCHSEARCH_Q&limit=$BRANCHSEARCH_LIMIT&offset=$OFFSET_LIMIT"

runTests() {
	echo "\n ================================================================= \n"
	echo "Test Run 1 \n"
	echo "Running autocomplete API endpoint (/api/branches/autocomplete) \n"
	curl $AUTOCOMPLETE_URL
	echo "\n ================================================================= \n"
	echo "Test Run 2 \n"
        echo "Running branch search API endpoint (/api/branches) \n"
	curl $BRANCHSEARCH_URL
	echo "\n ================================================================= \n"
}

runTests
