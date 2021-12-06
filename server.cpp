#include <iostream>
#include <stdio.h>

#include <array>

#include <oscpp/server.hpp>
#include <oscpp/print.hpp>

#include "udp.hpp"

using namespace udp_client_server;
using namespace std;

const size_t MAX_PACKET_SIZE = 8192;

void handlePacket(const OSCPP::Server::Packet &packet) {
  if (packet.isBundle()) {
    // Convert to bundle
    OSCPP::Server::Bundle bundle(packet);

    // Print the time
    std::cout << "#bundle " << bundle.time() << std::endl;

    // Get packet stream
    OSCPP::Server::PacketStream packets(bundle.packets());

    // Iterate over all the packets and call handlePacket recursively.
    // Cuidado: Might lead to stack overflow!
    while (!packets.atEnd()) {
      handlePacket(packets.next());
    }
  } else {
    // Convert to message
    OSCPP::Server::Message msg(packet);

    // Get argument stream
    OSCPP::Server::ArgStream args(msg.args());

    // Directly compare message address to string with operator==.
    // For handling larger address spaces you could use e.g. a
    // dispatch table based on std::unordered_map.
    if (msg == "/filter") {
      std::cout << "/filter"
                << " " << args.float32() << endl;
    } else if (msg == "/multi") {
      const char *name = args.string();
      const int32_t id = args.int32();
      std::cout << "/multi"
                << " " << name << " " << id << " ";
      std::cout << std::endl;
    } else {
      // Simply print unknown messages
      std::cout << "Unknown message: " << msg << std::endl;
    }
  }
}

int main() {
    std::array<char, MAX_PACKET_SIZE> buffer;
    udp_server server{"127.0.0.1", 3226};

    while (true) {
        int size = server.recv(buffer.data(), 1024);

        handlePacket(OSCPP::Server::Packet(buffer.data(), size));
    }

    return 0;
}