import argparse
import flwr as fl

def main(args):
    # Start Flower server
    fl.server.start_server(
        server_address=args.server_address,
        config=fl.server.ServerConfig(num_rounds=args.num_rounds),
    )

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--server_address", default="0.0.0.0:8080", type=str)
    parser.add_argument("--num_rounds", default=3, type=int)
    args = parser.parse_args()
    main(args)
