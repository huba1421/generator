from config import GENERATED_WALLETS_JSON_PATH, WALLETS_TO_GENERATE_COUNT
from wallet import Wallet
from generate_wallet import GenerateWallet
from flie import write_to_json


class GenerateWallets:
    @staticmethod
    def generate():
        generator = GenerateWallet()
        wallets = list()

        print("Running ArgentX wallets generator")
        print(f"Trying to generate {WALLETS_TO_GENERATE_COUNT} wallets")
        for i in range(WALLETS_TO_GENERATE_COUNT):
            wallet = generator.get_wallet_data()
            wallet_model = Wallet(
                private_key=wallet["private_key"],
                address=wallet["address"],
                seed=wallet["seed"],
            )
            wallets.append(wallet_model.__dict__)


        print(f"Wallets are generated. Saving to {GENERATED_WALLETS_JSON_PATH}")
        write_to_json(GENERATED_WALLETS_JSON_PATH, wallets)
