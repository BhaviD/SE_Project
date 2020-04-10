from graphql_client import gql, client

def downvote_answer(aId):
    downvote = gql('''
        mutation {
            update_Answers(
                where: {
                    Id: { _eq: ''' + str(aId) + ''' }
                }, 
                _inc: { VoteCount: -1 }
            ) {
                returning { VoteCount }
            }
        }
    ''')

    try:
        mutation_result = client.execute(downvote)
        print (mutation_result)
    except Exception as e:
        print (e)

if __name__ == "__main__":
    aId = 2
    downvote_answer(aId)